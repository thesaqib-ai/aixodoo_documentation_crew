import os
def main():
    # List of files to merge
    task_files = [
        'Requirements Report.md',
        'Odoo Models, Modules and Apps.md',
        'Odoo FIelds and Widgets.md',
        'Odoo Views.md',
        'Odoo PDF Report.md',
        'Odoo Automation Rules.md',
        'Odoo Approval Rules.md'
    ]

    # Output file for the unified report
    unified_report_file = 'Odoo Implementation Guide.md'

    def merge_markdown_files(files, output_file):
        """
        Merge multiple Markdown files into a single file.

        :param files: List of Markdown file paths to merge.
        :param output_file: Path to the output unified Markdown file.
        """
        with open(output_file, 'w') as outfile:
            for file in files:
                if os.path.exists(file):
                    with open(file, 'r') as infile:
                        # Write a header for each file section
                        outfile.write(f"## {os.path.splitext(os.path.basename(file))[0]}\n")
                        # Append the file content
                        outfile.write(infile.read())
                        # Add a blank line for separation
                        outfile.write("\n\n")
                else:
                    print(f"File not found: {file}")

    # Merge the files into the unified report
    merge_markdown_files(task_files, unified_report_file)
    print(f"Unified report created: {unified_report_file}")

if __name__ == "__main__":
    main()