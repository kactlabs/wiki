/ [Home](index.md)

## Kactii GenAI Peronsl Blog

**Note:** Where you can show off your GenAI skills

### Steps to Set Up Your Personal Blog

1. Visit the template repository at https://github.com/rajacsp/rajacsp.github.io

2. Create a new repository from the template by clicking "Use this template" on the top right green button, then select "Create a new repository"

3. Name your repository using your Github Handle. For example, if your Github link is like this "https://github.com/apgprem", create a repo like this: apgprem.github.io

4. Your final repository link would look like this: https://github.com/apgprem/apgprem.github.io

5. Open Terminal or Powershell and navigate to your workspace directory:
```
# Linux or Mac
cd ~/kactor

# window
cd c:\kact
```

6. Clone your newly created repository:
```
git clone git@github.com:apgprem/apgprem.github.io.git
```

7. Navigate into the cloned repository:
```
cd apgprem.github.io
```

8. Activate the conda environment:
```
conda activate test12
```

9. Install the required dependencies:
```
pip install -r requirements.txt
```

10. Start the local development server:
```
make devserver
```

11. Verify the app is running locally by opening your browser and visiting:
```
http://127.0.0.1:8000/
```

12. Publish your blog to make it live:
```
make publish
```

13. Sit back, relax, and enjoy a coffee or beer!

