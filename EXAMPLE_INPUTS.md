# Example Input Requirements for Testing

Use these example inputs when running your Verb Conjugator Factory application.

---

## 1. Simple Example (Recommended for First Test)

```
Create a simple English verb conjugator that supports present tense and past tense.
Include first person, second person, and third person singular forms.
```

**Why use this:**
- Quick to generate (~15 seconds)
- Easy to verify results
- Good for initial testing

---

## 2. Basic Two-Language Example

```
Build a verb conjugator for English and Spanish.
Support present tense, past tense, and future tense.
Include all six grammatical persons (first, second, third person in both singular and plural).
Handle both regular and irregular verbs.
```

**Why use this:**
- Shows multi-language capability
- Demonstrates irregular verb handling
- Good for demo video

---

## 3. Comprehensive Example (Best for Demo)

```
Create a Language Verb Conjugator application that supports English and Spanish.

Requirements:
- Support present tense, past tense, and future tense
- Handle both regular and irregular verbs
- Support first person singular, second person singular, and third person singular
- Provide a user-friendly Gradio interface where users can input a verb and see all conjugations
- Include comprehensive error handling for invalid inputs
- Display results in a clear, organized table format
```

**Why use this:**
- Very detailed requirements
- Shows all system capabilities
- Professional presentation
- Great for demo video

---

## 4. French Conjugator Example

```
Build a French verb conjugator with the following features:

Languages: French
Tenses: Present (présent), Imperfect (imparfait), Future (futur simple)
Persons: All six persons (je, tu, il/elle, nous, vous, ils/elles)
Special Requirements:
- Handle irregular French verbs like être, avoir, aller
- Include reflexive verbs
- Provide pronunciation hints if possible
```

**Why use this:**
- Tests single language focus
- Shows handling of complex grammar
- Demonstrates special requirements

---

## 5. Multi-Language Advanced Example

```
Create a comprehensive verb conjugator supporting English, Spanish, and French.

Tenses to support:
- Present tense
- Past tense (preterite for Spanish, passé composé for French)
- Future tense
- Conditional tense

Features:
- Support all grammatical persons (1st, 2nd, 3rd singular and plural)
- Handle irregular verbs in all languages
- Provide a dropdown menu to select language
- Display conjugation tables with clear labels
- Include example sentences for each conjugation
- Add error messages for verbs not found in the database
```

**Why use this:**
- Most comprehensive test
- Shows system handling complex requirements
- Good for final demo
- Tests all features

---

## 6. Minimalist Example

```
English verb conjugator. Present and past tense only. Simple interface.
```

**Why use this:**
- Tests minimal input handling
- Shows default behavior
- Quick generation

---

## 7. Educational Focus Example

```
Design a verb conjugator for language learning students.

Target: English and Spanish verbs
Tenses: Present, past, future
Features needed:
- Color-coded conjugation tables
- Highlight irregular forms in red
- Show verb stem changes
- Include practice mode where students can test themselves
- Provide hints for difficult conjugations
- Track which verbs the student has practiced
```

**Why use this:**
- Shows handling of specific use case
- Tests feature-rich requirements
- Demonstrates educational application

---

## 8. Professional/Business Example

```
Create a professional verb conjugation tool for translators and language professionals.

Languages: English, Spanish, French, Italian
Tenses: All major tenses including subjunctive and conditional moods
Requirements:
- Support for formal and informal forms (tú vs. usted in Spanish)
- Include regional variations (Latin American vs. European Spanish)
- Export conjugation tables to CSV format
- Batch processing for multiple verbs
- API endpoint for integration with other tools
```

**Why use this:**
- Tests handling of advanced requirements
- Shows system limitations (may not implement all features)
- Good for discussing challenges in report

---

## 9. Quick Test Example

```
Make a verb conjugator for English. Support present, past, and future tenses.
```

**Why use this:**
- Fastest generation
- Good for quick testing
- Minimal but complete

---

## 10. Detailed Specification Example (Recommended for Demo)

```
Language Verb Conjugator Application Specification

OVERVIEW:
Create a web-based verb conjugation tool for language learners.

SUPPORTED LANGUAGES:
- English
- Spanish

SUPPORTED TENSES:
- Present tense (presente)
- Past tense (pretérito)
- Future tense (futuro)
- Present perfect (pretérito perfecto)

GRAMMATICAL PERSONS:
- First person singular (I / yo)
- Second person singular (you / tú)
- Third person singular (he/she/it / él/ella)
- First person plural (we / nosotros)
- Second person plural (you all / vosotros)
- Third person plural (they / ellos/ellas)

VERB TYPES:
- Regular verbs (follow standard patterns)
- Irregular verbs (special conjugation rules)
- Stem-changing verbs (e→ie, o→ue, etc.)

USER INTERFACE REQUIREMENTS:
- Input field for verb entry
- Dropdown menu for language selection
- Dropdown menu for tense selection
- Button to generate conjugations
- Display results in a formatted table
- Show verb infinitive at the top
- Include "Clear" button to reset form

ERROR HANDLING:
- Validate that verb exists in database
- Show friendly error message for invalid verbs
- Handle empty input gracefully
- Provide suggestions for misspelled verbs

ADDITIONAL FEATURES:
- Show whether verb is regular or irregular
- Highlight the verb stem
- Include example sentences for each form
- Add pronunciation guide (optional)
- Support for copying results to clipboard
```

**Why use this:**
- Most professional format
- Very detailed requirements
- Shows system handling structured input
- Excellent for demo video
- Can discuss in report how system handles detailed specs

---

## Tips for Testing

### For Quick Testing:
Use examples 1, 6, or 9

### For Demo Video:
Use examples 3, 5, or 10

### For Showing Versatility:
Test multiple examples (1, 3, 7)

### For Report Discussion:
Use example 8 to discuss limitations

---

## What to Expect

### Generation Time:
- Simple examples: 15-20 seconds
- Complex examples: 25-35 seconds

### Generated Output:
- Python code for verb conjugator
- Gradio UI code
- 10-15 test cases
- Usage report with token counts

### Test Results:
- Expect 8-12 tests to pass (80%+ pass rate)
- Some tests may fail due to edge cases
- This is normal and acceptable

---

## Testing Workflow

1. **Start the application:**
   ```bash
   python main.py
   ```

2. **Open browser:**
   Navigate to `http://localhost:7860`

3. **Copy an example:**
   Choose one of the examples above

4. **Paste into text box:**
   Paste the requirements into the input field

5. **Click "Generate Application":**
   Wait for generation to complete

6. **Review outputs:**
   - Check Generated Code tab
   - Check Test Cases tab
   - Check Usage Report tab
   - Check Instructions tab

7. **Run generated app:**
   Follow instructions in the Instructions tab

8. **Test the conjugator:**
   Try verbs like:
   - English: "speak", "go", "be", "have"
   - Spanish: "hablar", "comer", "vivir", "ser"
   - French: "parler", "être", "avoir", "aller"

---

## Sample Verbs to Test Generated Applications

### English Regular Verbs:
- walk, talk, play, work, help, love, want, need

### English Irregular Verbs:
- be, have, do, go, see, make, take, come, know, get

### Spanish Regular Verbs:
- hablar (speak), comer (eat), vivir (live), trabajar (work)

### Spanish Irregular Verbs:
- ser (be), estar (be), ir (go), tener (have), hacer (do/make)

### French Regular Verbs:
- parler (speak), manger (eat), finir (finish)

### French Irregular Verbs:
- être (be), avoir (have), aller (go), faire (do/make)

---

## Recording Your Demo

When recording, use this sequence:

1. **Start with Example 1** (show it works quickly)
2. **Then use Example 3 or 10** (comprehensive demo)
3. **Show the generated code** (scroll through briefly)
4. **Show the test cases** (point out 10+ tests)
5. **Show usage report** (highlight token counts)
6. **Run the generated app** (test with real verbs)
7. **Run the tests** (show pytest output)

This gives a complete, professional demonstration!

---

## Troubleshooting

If generation fails:
- Try a simpler example first
- Check your API key is set correctly
- Verify internet connection
- Check the error message for details

If generated code doesn't run:
- This is expected sometimes (LLM limitations)
- Try regenerating with clearer requirements
- Manually fix small issues if needed
- Document in your report

---

**Good luck with your demo!** 🚀
