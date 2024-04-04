import sublate as sub


def main():
    print("[+] Building JetBrains theme")

    # make directories
    sub.mkdir("resources/schemes")
    sub.mkdir("src")

    # loop through themes and render the XML schemes and JSON themes
    for theme in sub.data["colors"]:
        for italics in [True, False]:
            scheme_file = f"{theme['id']}-{'no-' if not italics else ''}italics.xml"
            sub.render(
                f"resources/schemes/{scheme_file}",
                "templates/scheme.xml",
                {"theme": theme, "italics": italics},
            )

        sub.render(
            f"src/{theme['id']}.theme.json", "templates/theme.json", {"theme": theme}
        )

    # cleanup
    sub.rm("templates")
    sub.rm("build.py")


if __name__ == "__main__":
    main()
