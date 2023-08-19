from lxml import etree


# Task 3: Perform XML Validation
xml_doc = etree.parse("employees.xml")
xml_schema = etree.XMLSchema(file="employee_schema.xsd")

if xml_schema.validate(xml_doc):
    print("XML document is valid.")
else:
    print("XML document is not valid. Validation errors:")
    for error in xml_schema.error_log:
        print(f"Line {error.line}, Column {error.column}: {error.message}")
