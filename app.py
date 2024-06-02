from litestar import Litestar, get, post, Request
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
from litestar.response import Template
from pathlib import Path

# # Initialize the Litestar app with a Jinja template engine
# app = Litestar(template_engine=JinjaTemplateEngine(directory="templates"))

# Define a route to render the login page
@get("/")
async def login_page() -> Template:
    return Template("login.html")

# Define a route to handle the login logic
@post("/login")
async def login(request: Request) -> dict:
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")

    # Simple authentication logic (replace with your own logic)
    if username == "admin" and password == "secret":
        return {"message": "Login successful"}
    return {"message": "Invalid username or password"}

# Initialize the Litestar app with a Jinja template engine and register the routes
app = Litestar(
    route_handlers=[login_page, login],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    ),
)

# Run the Litestar app
if __name__ == "__main__":
    app.run(host='0.0.0.0')