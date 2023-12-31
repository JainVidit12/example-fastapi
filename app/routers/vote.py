from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, oath2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote, current_user : int = Depends(oath2.get_current_user), db: Session = Depends(database.get_db)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Post with id: {vote.post_id} does not exist")

    user_id = current_user.id
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == user_id)
    found_vote = vote_query.first()

    if vote.dir==1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                detail = f"user: {current_user.id} has already liked post with id: {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"message":"successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail = f"User with id: {current_user.id} has not previously liked post with id: {vote.post_id}")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message":"successfully deleted votes"}