from mlconjug3 import Conjugator

class VerbConjugator:
    """
    A class to conjugate verbs in French for specific tenses and persons.
    """

    def __init__(self, language='fr'):
        """
        Initializes the VerbConjugator.

        Args:
            language (str, optional): The language for conjugation.
                                      Defaults to 'fr' (French).
        """
        self.language = language
        try:
            self.conjugator = Conjugator(self.language)
        except Exception as e:
            print(f"Error initializing Conjugator for language '{self.language}': {e}")
            self.conjugator = None

    def conjugate(self, verb, tenses=None, persons=None):
        """
        Conjugates a given verb according to specified tenses and persons.

        Args:
            verb (str): The infinitive form of the verb to conjugate.
            tenses (list[str], optional): A list of tenses to conjugate.
                                          Valid options for French include:
                                          'indicatif présent', 'indicatif imparfait', 'indicatif futur simple'.
                                          If None, defaults to all supported tenses.
            persons (list[str], optional): A list of persons to conjugate.
                                           Valid options for French include:
                                           'je', 'tu', 'il', 'nous', 'vous', 'ils'.
                                           If None, defaults to all supported persons.

        Returns:
            dict: A dictionary where keys are tenses and values are dictionaries
                  mapping persons to their conjugated forms.
                  Returns an empty dictionary if conjugation fails.

        Raises:
            ValueError: If the provided language is not supported or initialization failed.
        """
        if not self.conjugator:
            raise ValueError(f"Conjugator not initialized for language '{self.language}'. Please check initialization.")

        # Define supported tenses and persons for French
        supported_tenses = {
            'present': 'indicatif présent',
            'imperfect': 'indicatif imparfait',
            'future': 'indicatif futur simple'
        }
        supported_persons = {
            'first_singular': 'je',
            'second_singular': 'tu',
            'third_singular': 'il',
            'first_plural': 'nous',
            'second_plural': 'vous',
            'third_plural': 'ils'
        }

        # Determine which tenses to use
        if tenses is None:
            selected_tenses = list(supported_tenses.values())
        else:
            selected_tenses = [supported_tenses.get(t.lower()) for t in tenses if t.lower() in supported_tenses]
            selected_tenses = [t for t in selected_tenses if t is not None] # Filter out unsupported tenses

        # Determine which persons to use
        if persons is None:
            selected_persons = list(supported_persons.values())
        else:
            selected_persons = [supported_persons.get(p.lower()) for p in persons if p.lower() in supported_persons]
            selected_persons = [p for p in selected_persons if p is not None] # Filter out unsupported persons

        conjugations = {}

        try:
            for tense in selected_tenses:
                tense_conjugations = {}
                for person in selected_persons:
                    try:
                        # mlconjug3 expects the full tense name and person as a string
                        # The format for mlconjug3 is often tense_person_structure
                        # For example: 'indicatif présent je', 'indicatif imparfait nous'
                        # We need to find the correct mlconjug3 internal representation if it differs.
                        # The library's get_conjugation method typically handles this.
                        # Let's access the verb object first.
                        verb_obj = self.conjugator.get_verb(verb)
                        if not verb_obj:
                            print(f"Warning: Verb '{verb}' not found or could not be processed.")
                            continue

                        # mlconjug3's get_conjugation method takes a full tense string
                        # and returns a dictionary for all persons for that tense.
                        # We then extract the specific person.
                        all_persons_for_tense = verb_obj.conjugate(tense)

                        if all_persons_for_tense and person in all_persons_for_tense:
                            tense_conjugations[person] = all_persons_for_tense[person]
                        else:
                            tense_conjugations[person] = "Not found" # Indicate if a specific person wasn't found for this tense

                    except Exception as e:
                        print(f"Error conjugating '{verb}' in tense '{tense}' for person '{person}': {e}")
                        tense_conjugations[person] = "Error"
                if tense_conjugations: # Only add tense if there were successful conjugations for it
                    conjugations[tense] = tense_conjugations

        except Exception as e:
            print(f"An unexpected error occurred during conjugation of '{verb}': {e}")
            return {}

        return conjugations

# Example Usage (optional, for testing purposes - not part of the module itself)
if __name__ == '__main__':
    conjugator = VerbConjugator(language='fr')

    # Conjugate 'manger' for present, imperfect, future, all persons
    print("--- Conjugating 'manger' (all tenses, all persons) ---")
    try:
        manger_conjugations_all = conjugator.conjugate('manger')
        for tense, persons in manger_conjugations_all.items():
            print(f"\n{tense.upper()}:")
            for person, form in persons.items():
                print(f"  {person}: {form}")
    except ValueError as e:
        print(e)

    print("\n" + "="*50 + "\n")

    # Conjugate 'aller' for present tense, first and third person singular/plural
    print("--- Conjugating 'aller' (present tense, specific persons) ---")
    try:
        aller_conjugations_specific = conjugator.conjugate('aller', tenses=['present'], persons=['first_singular', 'third_singular', 'first_plural', 'third_plural'])
        for tense, persons in aller_conjugations_specific.items():
            print(f"\n{tense.upper()}:")
            for person, form in persons.items():
                print(f"  {person}: {form}")
    except ValueError as e:
        print(e)

    print("\n" + "="*50 + "\n")

    # Example of an irregular verb ('être')
    print("--- Conjugating 'être' (imperfect, all persons) ---")
    try:
        etre_conjugations_imperfect = conjugator.conjugate('être', tenses=['imperfect'])
        for tense, persons in etre_conjugations_imperfect.items():
            print(f"\n{tense.upper()}:")
            for person, form in persons.items():
                print(f"  {person}: {form}")
    except ValueError as e:
        print(e)

    print("\n" + "="*50 + "\n")

    # Example with an unsupported tense
    print("--- Conjugating 'finir' (with an unsupported tense) ---")
    try:
        finir_conjugations_unsupported = conjugator.conjugate('finir', tenses=['present', 'past_perfect'])
        for tense, persons in finir_conjugations_unsupported.items():
            print(f"\n{tense.upper()}:")
            for person, form in persons.items():
                print(f"  {person}: {form}")
    except ValueError as e:
        print(e)

    print("\n" + "="*50 + "\n")

    # Example with an unsupported language (will raise an error during initialization)
    print("--- Trying to initialize with an unsupported language ---")
    try:
        unsupported_conjugator = VerbConjugator(language='es') # Spanish example
        # If initialization passes, try conjugating
        if unsupported_conjugator.conjugator:
            unsupported_conjugator.conjugate('hablar')
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("\n" + "="*50 + "\n")

    # Example with a verb not found
    print("--- Conjugating a non-existent verb ---")
    try:
        non_existent_conjugations = conjugator.conjugate('blabla')
        if not non_existent_conjugations:
            print("No conjugations found for 'blabla', as expected.")
    except ValueError as e:
        print(e)