import pypdf
import argparse
from typing import Optional
import re
import os

MAX_FILENAME_LENGTH = 255


def clean_title(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    cleaned = re.sub(r"\s+", "_", cleaned)
    return cleaned


def get_pdf_title(file_path: str) -> Optional[str]:
    with open(file_path, "rb") as file:
        reader = pypdf.PdfReader(file)
        info = reader.metadata
        title = info.title if info and info.title else None
        return title


def rename_file(file_path: str, new_title: str) -> None:
    directory, original_filename = os.path.split(file_path)
    _, ext = os.path.splitext(original_filename)

    # ファイル名を255文字に制限
    if len(new_title) > MAX_FILENAME_LENGTH - len(ext):
        new_title = new_title[: MAX_FILENAME_LENGTH - len(ext)]

    new_file_path = os.path.join(directory, f"{new_title}{ext}")

    os.rename(file_path, new_file_path)
    print(f"Renamed to:", new_file_path)


def rename_pdfs_in_directory(directory: str) -> None:
    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            title = get_pdf_title(file_path)
            if title is None:
                print(f"Title not found:", file_path)
                continue
            new_title = clean_title(title)
            rename_file(file_path, new_title)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename PDF files with underscores instead of special characters."
    )
    parser.add_argument("path", type=str, help="path to the PDF file or directory")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        rename_pdfs_in_directory(args.path)
    elif os.path.isfile(args.path):
        title = get_pdf_title(args.path)
        if title is None:
            print("Title not found:", args.path)
            return
        new_title = clean_title(title)
        rename_file(args.path, new_title)
    else:
        raise ValueError("The provided path is neither a file nor a directory")


if __name__ == "__main__":
    main()
