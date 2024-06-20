from fastapi import APIRouter, Depends
from app.schemas.example_schema import ExampleSchema
from app.services.example_service import ExampleService
from app.dependencies.example_dependency import get_example_service

router = APIRouter()

@router.get("/", response_model=ExampleSchema)
async def read_example(example_service: ExampleService = Depends(get_example_service)):
    return example_service.get_example()
