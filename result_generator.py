#create a MD to checkout puts from terminal and transfer results from it.
import subprocess

# Run the app.py script to generate regression results
result = subprocess.check_output(["python", "test.py"], text=True)

# Create a Markdown file with the results
markdown_content = f"""# Linear Regression Results

{result}
"""

with open("ML_pipeline_results.md", "w") as markdown_file:
    markdown_file.write(markdown_content)

print("Results saved to linear_regression_results.md")