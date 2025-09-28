import subprocess

def query_ollama(prompt: str, model: str = "phi"):
    """
    Query a local Ollama model (default: phi).
    
    Args:
        prompt (str): The text prompt to send to the model.
        model (str): The model to use (default = phi, can be changed to mistral, llama2, etc.)

    Returns:
        str: Model output as a string (cleaned if needed).
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode(),
            capture_output=True,
            check=True
        )
        output = result.stdout.decode().strip()

        # Clean possible code fences
        if output.startswith("```"):
            output = output.split("```")[1]
            output = output.replace("json", "").replace("python", "").strip()

        return output
    except subprocess.CalledProcessError as e:
        return f"Error running Ollama model {model}: {e.stderr.decode().strip()}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
