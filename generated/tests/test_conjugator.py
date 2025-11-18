import pytest
from verb_conjugator import conjugate_verb  # Assuming your conjugator is in verb_conjugator.py

# Define regular verb conjugation patterns for French (simplified for this example)
# In a real application, this would be more extensive.
REGULAR_VERBS_FRENCH = {
    "parler": {
        "present": {
            "je": "parle", "tu": "parles", "il": "parle", "nous": "parlons", "vous": "parlez", "ils": "parlent"
        },
        "imperfect": {
            "je": "parlais", "tu": "parlais", "il": "parlait", "nous": "parlions", "vous": "parliez", "ils": "parlaient"
        },
        "future": {
            "je": "parlerai", "tu": "parleras", "il": "parlera", "nous": "parlerons", "vous": "parlerez", "ils": "parleront"
        }
    },
    "finir": {
        "present": {
            "je": "finis", "tu": "finis", "il": "finit", "nous": "finissons", "vous": "finissez", "ils": "finissent"
        },
        "imperfect": {
            "je": "finissais", "tu": "finissais", "il": "finissait", "nous": "finissions", "vous": "finissiez", "ils": "finissaient"
        },
        "future": {
            "je": "finirai", "tu": "finiras", "il": "finira", "nous": "finirons", "vous": "finirez", "ils": "finiront"
        }
    }
}

# Define irregular verb conjugations for French (common examples)
IRREGULAR_VERBS_FRENCH = {
    "être": {
        "present": {
            "je": "suis", "tu": "es", "il": "est", "nous": "sommes", "vous": "êtes", "ils": "sont"
        },
        "imperfect": {
            "je": "étais", "tu": "étais", "il": "était", "nous": "étions", "vous": "étiez", "ils": "étaient"
        },
        "future": {
            "je": "serai", "tu": "seras", "il": "sera", "nous": "serons", "vous": "serez", "ils": "seront"
        }
    },
    "avoir": {
        "present": {
            "je": "ai", "tu": "as", "il": "a", "nous": "avons", "vous": "avez", "ils": "ont"
        },
        "imperfect": {
            "je": "avais", "tu": "avais", "il": "avait", "nous": "avions", "vous": "aviez", "ils": "avaient"
        },
        "future": {
            "je": "aurai", "tu": "auras", "il": "aura", "nous": "aurons", "vous": "aurez", "ils": "auront"
        }
    },
    "aller": {
        "present": {
            "je": "vais", "tu": "vas", "il": "va", "nous": "allons", "vous": "allez", "ils": "vont"
        },
        "imperfect": {
            "je": "allais", "tu": "allais", "il": "allait", "nous": "allions", "vous": "alliez", "ils": "allaient"
        },
        "future": {
            "je": "irai", "tu": "iras", "il": "ira", "nous": "irons", "vous": "irez", "ils": "iront"
        }
    }
}

# Helper function to generate test cases from data
def generate_conjugation_tests(verbs_data, language, tenses):
    test_cases = []
    for verb, tenses_data in verbs_data.items():
        for tense in tenses:
            if tense in tenses_data:
                for pronoun, conjugation in tenses_data[tense].items():
                    test_cases.append(
                        (language, verb, tense, pronoun, conjugation)
                    )
    return test_cases

# Generate test data for French regular verbs
french_regular_test_data = generate_conjugation_tests(
    REGULAR_VERBS_FRENCH, "french", ["present", "imperfect", "future"]
)

# Generate test data for French irregular verbs
french_irregular_test_data = generate_conjugation_tests(
    IRREGULAR_VERBS_FRENCH, "french", ["present", "imperfect", "future"]
)

# Combine all valid test cases
all_valid_test_cases = french_regular_test_data + french_irregular_test_data

@pytest.mark.parametrize(
    "language, verb, tense, pronoun, expected_conjugation",
    all_valid_test_cases
)
def test_valid_verb_conjugations(language, verb, tense, pronoun, expected_conjugation):
    """
    Tests valid verb conjugations for French regular and irregular verbs
    across different tenses and pronouns.
    """
    print(f"\nTesting: Language='{language}', Verb='{verb}', Tense='{tense}', Pronoun='{pronoun}'")
    actual_conjugation = conjugate_verb(language, verb, tense, pronoun)
    assert actual_conjugation == expected_conjugation, \
        f"For {verb} ({tense}, {pronoun}) in {language}, expected '{expected_conjugation}', but got '{actual_conjugation}'"

# --- Error Handling Tests ---

def test_invalid_language():
    """
    Tests error handling for an unsupported language.
    """
    print("\nTesting invalid language input.")
    with pytest.raises(ValueError, match="Unsupported language: spanish"):
        conjugate_verb("spanish", "parler", "present", "je")

def test_invalid_tense():
    """
    Tests error handling for an unsupported tense.
    """
    print("\nTesting invalid tense input.")
    with pytest.raises(ValueError, match="Unsupported tense: past"):
        conjugate_verb("french", "parler", "past", "je")

def test_verb_not_found():
    """
    Tests error handling for a verb not in the conjugator's dictionary.
    """
    print("\nTesting verb not found.")
    with pytest.raises(KeyError, match="Verb 'inventer' not found in conjugation data."):
        conjugate_verb("french", "inventer", "present", "je")

def test_pronoun_not_found():
    """
    Tests error handling for an unsupported pronoun.
    """
    print("\nTesting pronoun not found.")
    with pytest.raises(KeyError, match="Pronoun 'moi' not found for verb 'parler' in 'present' tense."):
        conjugate_verb("french", "parler", "present", "moi")

# --- Edge Case Tests ---

def test_case_insensitivity_verb():
    """
    Tests if verb conjugation is case-insensitive for the verb input.
    """
    print("\nTesting case insensitivity for verb input.")
    verb = "PARLER"
    language = "french"
    tense = "present"
    pronoun = "je"
    expected_conjugation = REGULAR_VERBS_FRENCH["parler"]["present"]["je"]
    actual_conjugation = conjugate_verb(language, verb, tense, pronoun)
    assert actual_conjugation == expected_conjugation, \
        f"Case insensitivity failed for verb '{verb}'. Expected '{expected_conjugation}', got '{actual_conjugation}'"

def test_case_insensitivity_pronoun():
    """
    Tests if pronoun input is case-insensitive.
    """
    print("\nTesting case insensitivity for pronoun input.")
    verb = "être"
    language = "french"
    tense = "present"
    pronoun = "IL"
    expected_conjugation = IRREGULAR_VERBS_FRENCH["être"]["present"]["il"]
    actual_conjugation = conjugate_verb(language, verb, tense, pronoun)
    assert actual_conjugation == expected_conjugation, \
        f"Case insensitivity failed for pronoun '{pronoun}'. Expected '{expected_conjugation}', got '{actual_conjugation}'"

def test_edge_case_empty_string_inputs():
    """
    Tests behavior with empty string inputs for verb, tense, or pronoun.
    These should ideally raise errors.
    """
    print("\nTesting edge case with empty string inputs.")
    with pytest.raises(ValueError): # Or specific error if your conjugator handles empty strings differently
        conjugate_verb("french", "", "present", "je")
    with pytest.raises(ValueError):
        conjugate_verb("french", "parler", "", "je")
    with pytest.raises(ValueError):
        conjugate_verb("french", "parler", "present", "")

def test_verb_ending_in_er_imperfect():
    """
    Tests a regular verb ending in -er in the imperfect tense.
    """
    print("\nTesting regular verb ending in -er in imperfect tense.")
    language = "french"
    verb = "jouer" # Another regular verb
    tense = "imperfect"
    pronoun = "nous"
    # Expected: jouions
    expected_conjugation = "jouions"
    actual_conjugation = conjugate_verb(language, verb, tense, pronoun)
    assert actual_conjugation == expected_conjugation, \
        f"Imperfect conjugation failed for '{verb}'. Expected '{expected_conjugation}', got '{actual_conjugation}'"

# Additional test case to ensure coverage of irregular verbs not explicitly listed in parameterized tests
def test_specific_irregular_conjugation():
    """
    Tests a specific, less common irregular conjugation for thoroughness.
    """
    print("\nTesting specific irregular conjugation for 'savoir'.")
    language = "french"
    verb = "savoir"
    tense = "future"
    pronoun = "vous"
    # Expected: saurez
    expected_conjugation = "saurez"
    # This verb needs to be added to IRREGULAR_VERBS_FRENCH for this test to pass if not already there.
    # For demonstration purposes, assuming it might exist or you'd add it.
    # If 'savoir' is not in your actual IRREGULAR_VERBS_FRENCH, this test will fail as expected if it's a verb you intend to conjugate.
    try:
        actual_conjugation = conjugate_verb(language, verb, tense, pronoun)
        assert actual_conjugation == expected_conjugation, \
            f"Future conjugation failed for '{verb}'. Expected '{expected_conjugation}', got '{actual_conjugation}'"
    except KeyError:
        pytest.skip(f"Verb '{verb}' not implemented in the conjugator for testing.")