ex00
for check
1.Check Argument Handling -Try running the script without an argument:
    python3 render.py

2.Test Incorrect File Extension with an incorrect file extension (e.g., .txt or .csv instead of .template):

    python3 render.py myCv.txt

3.Test Non-Existent File - Run the script with a non-existent file:
    python3 render.py nonexistent.template
    
4.Test Multiple Arguments - Run the script with more than one argument:

    python3 render.py myCv.template extra_arg
    
5 Check Your Python Script

    python3 render.py myCv.template
    To confirm correct output, run:
    cat myCv.html
6.Validate Settings Change - Modify settings.py:
        name = "NewName"
        surname = "UpdatedSurname"
        age = 25
        profession = "Software Engineer"
    after changment 
        python3 render.py myCv.template, 
    Check if myCv.html updates correctly with new values.

7. Debug Potential Errors - If no output file is generated, check for mistakes:
 8. Ensure Clean Code Execution - Check for syntax issues:
 
    python3 -m py_compile render.py



