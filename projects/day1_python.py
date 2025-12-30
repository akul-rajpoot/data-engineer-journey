print("VS Code is ready 🚀")
def analyze_numbers(nums):
    return {
        "sum": sum(nums),
        "avg": sum(nums)/len(nums),
        "max": max(nums),
        "min": min(nums)
    }
def word_lengths(words):
    return {w: len(w) for w in words}
print(analyze_numbers([10,20,30,40]))
print(word_lengths(["data","engineer","python"]))