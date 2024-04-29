def frequency_analysis_affine(ciphertext):
    # Frequency analysis on digraphs
    digraphs_frequency = {}
    for i in range(len(ciphertext) - 1):
        digraph = ciphertext[i:i+2]
        if digraph.isalpha():
            if digraph in digraphs_frequency:
                digraphs_frequency[digraph] += 1
            else:
                digraphs_frequency[digraph] = 1
    sorted_digraphs = sorted(digraphs_frequency.items(), key=lambda x: x[1], reverse=True)
    print("Most common digraphs:")
    for digraph, frequency in sorted_digraphs[:5]:
        print(f"Digraph: {digraph}, Frequency: {frequency}")

ciphertext = "UWRGRO"
frequency_analysis_affine(ciphertext)