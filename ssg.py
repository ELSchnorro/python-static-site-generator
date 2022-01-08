import typer
from ssg.site import site

def main(source = "content", dest = "dist"):
    configure = {"source":source, "dest":dest}
    site(**configure).build()

typer.run(main)  