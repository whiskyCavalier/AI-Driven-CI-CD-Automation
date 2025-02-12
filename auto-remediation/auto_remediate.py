import openai
import subprocess
import time

openai.api_key = "your_openai_api_key"

def get_failed_pods():
    result = subprocess.run(["kubectl", "get", "pods", "--field-selector=status.phase!=Running"], capture_output=True, text=True)
    return result.stdout

def analyze_logs(logs):
    prompt = f"Analyze these Kubernetes logs and suggest a fix:\n\n{logs}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def restart_failed_pods():
    pods = get_failed_pods()
    if pods:
        print(f"Restarting failed pods:\n{pods}")
        subprocess.run(["kubectl", "delete", "pod", "--all"])

if __name__ == "__main__":
    while True:
        failed_pods = get_failed_pods()
        if failed_pods:
            print("⚠️ Detected failed pods! Analyzing logs...")
            fix_suggestions = analyze_logs(failed_pods)
            print("AI Suggested Fix:", fix_suggestions)
            print("🚀 Restarting failed pods...")
            restart_failed_pods()
        time.sleep(60)  # Check every minute
    