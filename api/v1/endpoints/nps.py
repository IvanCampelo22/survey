from fastapi import BackgroundTasks, APIRouter, HTTPException

from apps.schemas.nps_schemas import EmailSchema, SurveySchema, ScaleChoice
from apps.services.nps_service import send_email_async

router = APIRouter()

fake_db = {
    "survey": {"id": "2", "title": "NPS", "description": "Pesquisa de satisfação", "question": [""]},
    "scale": {"id": "1", "question": "Qual sua opinião sobre a charisma?", "scale": 6},
    "sigleChoice": {"id": "1", "question": "teste"}
}

@router.post("/send-email/")
async def send_email(background_tasks: BackgroundTasks, email: EmailSchema):
    background_tasks.add_task(send_email_async, email.email, email.subject, email.message)
    return {"message": "Email sent successfully"}


@router.post("/survey/")
async def survey(survey: SurveySchema):
    return survey

# @router.get("/survey/")
# async def get_survey(survey: SurveySchema):
#     ...

@router.get("/get-survey/", response_model=SurveySchema)
async def read_survey():
    pass

@router.post("/survey/scale")
async def scale(scale: ScaleChoice):
    fake_db[scale.id] = scale
    return scale