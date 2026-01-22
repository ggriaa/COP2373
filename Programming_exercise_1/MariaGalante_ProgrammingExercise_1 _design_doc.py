import inspect
import MariaGalante_ProgrammingExercise_1


with open("MariaGalante_ProgrammingExercise_1_design_doc.txt", "w") as doc:

    doc.write(
        f"# Technical Design Document: "
        f"{MariaGalante_ProgrammingExercise_1.__name__}\n\n"
    )

    doc.write("# Name: Maria Galante\n")
    doc.write("# Date: January 21, 2026\n")
    doc.write(
        "# Program Description: This program simulates the pre-sale of cinema "
        "tickets with purchase limits and input validation.\n\n"
    )

    for name, func in inspect.getmembers(
        MariaGalante_ProgrammingExercise_1,
        inspect.isfunction
    ):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    doc.write(
        "# Link to your repository: https://github.com/ggriaa/COP2373\n"
    )

print("Complete")
