#!/usr/bin/env python
import streamlit as st
from aixodoo.crew import AixodooCrew
import os

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
                    outfile.write(f"# {os.path.splitext(os.path.basename(file))[0]}\n")
                    # Append the file content
                    outfile.write(infile.read())
                    # Add a blank line for separation
                    outfile.write("\n\n")
            else:
                st.warning(f"File not found: {file}")

def generate_unified_report():
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
    unified_report_file = 'Odoo Implementation Guide.md'

    # Merge the files into the unified report
    merge_markdown_files(task_files, unified_report_file)
    return unified_report_file

def run():
    st.title("AixodooCrew Business Requirement Interface")

    st.sidebar.title("Options")
    page = st.sidebar.radio("Select Action", ["Write Requirements", "Run Crew", "View Report"])

    if page == "Write Requirements":
        st.header("Write Business Requirements")
        requirements = st.text_area(
            "Enter your business requirements here:",
            height=300,
            placeholder="Write detailed business requirements..."
        )

        if st.button("Save Requirements"):
            with open("requirements.txt", "w") as f:
                f.write(requirements)
            st.success("Requirements saved successfully!")

    elif page == "Run Crew":
        st.header("Execute AixodooCrew")
        if st.button("Run Crew"):
            try:
                # Read the saved requirements
                with open("requirements.txt", "r") as f:
                    requirements = f.read()

                def convert_to_single_line(text):
                    return " ".join(text.splitlines()).strip()

                inputs = {'business requirement': convert_to_single_line(requirements)}
                AixodooCrew().crew().kickoff(inputs=inputs)

                # Generate the unified report
                report_path = generate_unified_report()
                st.success("Crew executed successfully!")
                st.info(f"Unified report created: {report_path}")

            except Exception as e:
                st.error(f"An error occurred: {e}")

    elif page == "View Report":
        st.header("View Odoo Implementation Guide")
        report_path = "Odoo Implementation Guide.md"
        if os.path.exists(report_path):
            with open(report_path, "r") as f:
                report_content = f.read()
            st.markdown(report_content)
        else:
            st.warning("Unified report not found. Please run the crew first.")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'business requirement' : "A mid-sized manufacturing company specializing in custom furniture seeks to implement Odoo ERP to streamline its operations. The project involves integrating the Finance, Inventory, Production, and E-commerce modules using Odoo Studio 17, aiming to automate processes, enhance data visibility, and provide a unified system for managing all aspects of the business. 1. Business Case Overview: The company produces custom furniture and requires an integrated solution that manages financial operations, tracks inventory in real-time, schedules production, and integrates with an e-commerce platform for online sales. 2. Detailed Functional Requirements: - Finance Module: Automate the creation of monthly financial statements, including income statements, balance sheets, and cash flow reports. Implement an invoicing system that supports automated invoicing based on sales orders and tracks payments in real-time. Set up expense tracking with automated categorization and approval workflows. Configure financial reporting dashboards for real-time financial performance insights. - Inventory Module: Enable real-time inventory tracking across multiple warehouses, integrating with sales orders and purchase orders. Create an automated low-stock alert system that notifies the purchasing department when inventory levels fall below a defined threshold. Integrate the inventory module with the e-commerce platform to automatically update stock levels based on online sales and returns. Set up inventory valuation using FIFO (First In, First Out) method and automate periodic stock reconciliation processes. - Production Module: Design a system for creating and managing production orders, with automated work-in-progress (WIP) tracking and status updates. Implement a scheduling system that automatically plans production runs based on incoming sales orders and material availability. Integrate production management with the inventory module to ensure that raw materials are reserved and available before scheduling production. Configure automated alerts for production delays or material shortages, providing visibility into potential bottlenecks. - E-commerce Module: Integrate the e-commerce platform with the inventory and sales modules to provide real-time stock updates and streamline order fulfillment. Enable automated syncing of product listings, prices, and stock levels between the e-commerce platform and Odoo ERP. Set up an automated order confirmation and invoicing process for online sales, reducing manual intervention. Implement customer data synchronization between the e-commerce platform and CRM for unified customer management. 3. Current Pain Points and Automation Needs: The company currently faces issues with manual invoicing, resulting in frequent errors and delays in payment processing. Automation is needed to reduce errors and speed up the invoicing process. Inventory management is handled using spreadsheets, causing discrepancies and a lack of real-time visibility into stock levels. Implementing real-time inventory tracking and automated stock alerts will address this issue. Production scheduling lacks coordination with inventory availability, leading to delays and missed delivery deadlines. Automating production planning based on sales orders and inventory levels will streamline scheduling and improve on-time delivery rates. The lack of integration between the e-commerce platform and back-end systems results in delayed updates to stock levels, affecting customer satisfaction. Seamless integration between the e-commerce platform and Odoo ERP is required for real-time stock updates and order processing. 4. Implementation Considerations: Use Odoo Studio 17 to customize modules, set up automated workflows, and design custom views for each functional area. Ensure the solution is scalable to accommodate future growth, including additional product lines and increased sales volume. Focus on user training and documentation to facilitate a smooth transition from the current manual processes to the new automated system."
    }
    try:
        AixodooCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AixodooCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        AixodooCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

if __name__ == "__main__":
    run()

