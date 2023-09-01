from ninja import NinjaAPI

from courses.api import router as courses_router
from reviews.api import router as reviews_router
from schools.api import router as school_router
from search.api import router as search_router

api = NinjaAPI(
    title="Skillhub API",
    description="This is a Skillhub API with dynamic OpenAPI info section",
    version='1',
)

api.add_router('/courses/', courses_router, tags=["Courses"])
api.add_router('/reviews/', reviews_router, tags=["Reviews"])
api.add_router('/schools/', school_router, tags=["Schools"])
api.add_router('/search/', search_router, tags=["Search"])
