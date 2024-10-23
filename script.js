async function handleTranslation() {
    const textInput = document.getElementById('textInput').value;
    const response = await fetch('/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: textInput })
    });
  
    const data = await response.json();
    document.getElementById('translatedOutput').textContent = data.translated_text;
  
    const suggestionsList = document.getElementById('suggestionsList');
    suggestionsList.innerHTML = '';  // Clear previous suggestions
  
    for (const [lang, suggestion] of Object.entries(data.suggestions)) {
      const listItem = document.createElement('li');
      listItem.textContent = `${lang}: ${suggestion.translated}`;
      suggestionsList.appendChild(listItem);
    }
  }
  
  function recordSpeech() {
    alert("Speech-to-text feature coming soon!");  // Placeholder for now
  }
  