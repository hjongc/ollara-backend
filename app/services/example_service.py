from app.schemas.example_schema import ExampleSchema

class ExampleService:
    def get_example(self) -> ExampleSchema:
        return ExampleSchema(id=1, name="Example", description="This is an example")
