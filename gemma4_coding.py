from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import time
import subprocess
import os

MODEL_REPO = "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF"
MODEL_FILE = "gemma4-coding-Q4_K_M.gguf"

print("=" * 80)
print("GEMMA 4 12B EVALUATION")
print("=" * 80)

# GPU INFO
try:
    gpu_info = subprocess.check_output(
        "nvidia-smi --query-gpu=name,memory.total --format=csv,noheader",
        shell=True
    ).decode().strip()
except:
    gpu_info = "GPU Not Found"

print("GPU:", gpu_info)

# Download Model
print("\nDownloading Model...")

model_path = hf_hub_download(
    repo_id=MODEL_REPO,
    filename=MODEL_FILE
)

# Load Model
print("Loading Model...")

load_start = time.time()

llm = Llama(
    model_path=model_path,
    n_gpu_layers=-1,
    n_ctx=4096,
    n_batch=512,
    verbose=False
)

load_end = time.time()

load_time = round(load_end - load_start, 2)

print(f"Model Load Time: {load_time} sec")

prompts = [
    "Write a Python function to reverse a string.",
    "Write SQL query to find second highest salary.",
    "Explain RAG architecture with example.",
    "Explain LangGraph vs LangChain.",
    "Solve Two Sum problem in Python."
]

os.makedirs("results", exist_ok=True)

report = open(
    "results/evaluation_report.txt",
    "w",
    encoding="utf-8"
)

report.write("GEMMA 4 T4 EVALUATION REPORT\n")
report.write("=" * 80 + "\n")

for i, prompt in enumerate(prompts, start=1):

    print("\n" + "=" * 80)
    print(f"TEST {i}")
    print("=" * 80)

    start_time = time.time()

    response = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=512
    )

    end_time = time.time()

    answer = response["choices"][0]["message"]["content"]

    usage = response.get("usage", {})

    prompt_tokens = usage.get("prompt_tokens", 0)
    completion_tokens = usage.get("completion_tokens", 0)
    total_tokens = usage.get("total_tokens", 0)

    latency = round(end_time - start_time, 2)

    tokens_per_sec = (
        round(completion_tokens / latency, 2)
        if latency > 0 else 0
    )

    print(prompt)
    print(f"Latency: {latency}s")
    print(f"Tokens/sec: {tokens_per_sec}")

    report.write(f"\nTEST {i}\n")
    report.write(f"Prompt: {prompt}\n")
    report.write(f"Prompt Tokens: {prompt_tokens}\n")
    report.write(f"Completion Tokens: {completion_tokens}\n")
    report.write(f"Total Tokens: {total_tokens}\n")
    report.write(f"Latency: {latency}\n")
    report.write(f"Tokens/sec: {tokens_per_sec}\n")
    report.write("-" * 60 + "\n")

report.close()

print("\nReport Saved:")
print("results/evaluation_report.txt")
