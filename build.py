#!/usr/bin/env python3
import sublate as sub


def main():
    # update data dictionary with the current date and color themes
    sub.data.update(
        {
            "date": sub.date_iso(),
            "colors": sub.read("colors/*.yaml").values(),
        }
    )

    # clean output directory and copy the theme templates over
    sub.rm("output")
    sub.cp("theme", "output")

    # execute build scripts themes in the output directory
    sub.run("output/*/build.py")


if __name__ == "__main__":
    main()
