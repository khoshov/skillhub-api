from ninja import NinjaAPI
from courses.api import router as courses_router

api = NinjaAPI()

api.add_router('/courses/', courses_router)
