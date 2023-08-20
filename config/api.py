from ninja import NinjaAPI

from courses.api import router as courses_router
from schools.api import router as school_router

api = NinjaAPI(
   openapi_extra={
        "info": {
            "version": 1.1,
        }
    },
   title="Skillhub API",
   description="This is a Skillhub API with dynamic OpenAPI info section"
)

api.add_router('/courses/', courses_router, tags=["Courses"])
api.add_router('/schools/', school_router, tags=["Schools"])
