import os

def auto_fix(project_root):

    fixes = []

    for root, dirs, files in os.walk(project_root):

        for file in files:

            if not file.endswith(".py"):
                continue

            filepath = os.path.join(
                root,
                file
            )

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as f:

                content = f.read()

            new_content = content

            new_content = new_content.replace(
                "from app.",
                "from generated_code.app."
            )

            if new_content != content:

                with open(
                    filepath,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(new_content)

                fixes.append(
                    filepath
                )

    return fixes