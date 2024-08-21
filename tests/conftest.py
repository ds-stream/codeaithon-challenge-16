import pytest
import os, sys
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine


def pytest_addoption(parser):
    parser.addoption("--developer", action="store", default="default_value")


@pytest.fixture(scope="session", autouse=True)
def developer(request):
    developer_id = request.config.getoption("--developer")
    # Dynamically determine the developer ID
    print(f"Running tests for developer-{developer_id}")
    print(f"Current path is {os.getcwd()}")
    # Construct the path to the developer's source code
    source_path = os.path.join(
        os.getcwd(), f"submissions/developer-{developer_id}/results/"
    )

    # Add the path to sys.path if it's not already there
    if source_path not in sys.path:
        print(f"Adding source path {source_path} to sys.path")
        sys.path.insert(0, source_path)
    print(sys.path)

    return developer_id


@pytest.fixture(scope="session")
def developer_app(pytestconfig):
    developer_id = pytestconfig.getoption("--developer")

    if developer_id:
        # Construct the dynamic path based on the developer ID
        path = os.path.abspath(f"submissions/developer-{developer_id}/results/app/")

        # Insert the path at the beginning of sys.path
        sys.path.insert(0, path)
        print(f"Dynamically added {path} to PYTHONPATH")

        # Dynamically import the FastAPI app from the developer-specific path
        try:
            global app
            app_module = __import__("main", fromlist=["main"])
            app = getattr(app_module, "app")
            return app
        except ModuleNotFoundError as e:
            raise pytest.UsageError(f"Could not import FastAPI app from {path}: {e}")
    else:
        raise pytest.UsageError("--developer option is required.")


@pytest.fixture(scope="session")
def client(developer_app):
    # Create a test database
    from database import get_session

    TEST_DATABASE_URL = "sqlite:///./test_database.db"
    test_engine = create_engine(TEST_DATABASE_URL, echo=True)

    # Override the get_session function to use the test database
    def override_get_session():
        with Session(test_engine) as session:
            yield session

    developer_app.dependency_overrides[get_session] = override_get_session
    # Create the test database and tables
    SQLModel.metadata.create_all(test_engine)

    return TestClient(developer_app)
