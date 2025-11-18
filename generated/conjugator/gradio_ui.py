import gradio as gr
from verb_conjugator import Conjugator

def conjugate_verb(verb, language, tense):
    """
    Conjugates a verb based on language and tense using the verb_conjugator module.

    Args:
        verb (str): The infinitive verb to conjugate.
        language (str): The language of the verb (e.g., "French").
        tense (str): The tense to conjugate in (e.g., "present", "imperfect", "future").

    Returns:
        str: A formatted string of conjugation results or an error message.
    """
    try:
        if language.lower() == "french":
            conjugator = Conjugator(language.lower())
            supported_tenses = ["present", "imperfect", "future"]
            if tense.lower() not in supported_tenses:
                return f"Error: Tense '{tense}' not supported for French. Supported tenses are: {', '.join(supported_tenses)}."

            result = conjugator.conjugate(verb, tense)

            if not result:
                return f"Could not conjugate '{verb}' in the {tense} tense for French."

            output_str = f"## Conjugation of '{verb}' in {language} - {tense.capitalize()} Tense:\n\n"
            for person, forms in result.items():
                output_str += f"**{person.capitalize()}**: {', '.join(forms)}\n"
            return output_str
        else:
            return f"Error: Language '{language}' is not supported. Currently, only 'French' is supported."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Define supported languages and tenses for the dropdowns
supported_languages = ["French"]
supported_tenses = ["present", "imperfect", "future"]

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Verb Conjugator")
    gr.Markdown("Enter a verb, select the language and tense to see its conjugation.")

    with gr.Row():
        verb_input = gr.Textbox(label="Verb (infinitive)", placeholder="e.g., parler")
        language_input = gr.Dropdown(choices=supported_languages, label="Language", value="French")
        tense_input = gr.Dropdown(choices=supported_tenses, label="Tense", value="present")

    conjugate_button = gr.Button("Conjugate")

    output_text = gr.Textbox(label="Conjugation Results", interactive=False, lines=10)

    conjugate_button.click(
        conjugate_verb,
        inputs=[verb_input, language_input, tense_input],
        outputs=output_text
    )

if __name__ == "__main__":
    demo.launch()