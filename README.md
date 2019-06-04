# SentimentalAnalysysKIP
Project to run a sentimental analysis and explore the results in a KIP Case

## Structure
The Scripts are divided according to the step in which they were used and applied

1. Pre-process: Extract message bodies from sql, clear texts, removing redudant text(e-mail history and signature), clearing extra information(email, phone, tags, urls) and translate using Google Sheets

2. Dictionary: Mount custom dictionary from seeds. First expand using WorldNet, then cut using SentiWordNet and relating sentimental scores

3. SentimentalAnalysis: Execute sentimental analysis process. First prepare dictionary(setting expressions and correcting values) and base(Joining expressions, normalizing capitalization and removing invalid chars). Then execute process, using tokenization, lemmatization and processing punctuation. In the end, classification message according to final score.

4. EmotionAnalysis: First prepare original NCR dictionary to standard configuration, then use it to assign values to custom dictionary. Then prepare base(similar to sentimental analysis) and execute the emotion analysis using generated mapping.

5. TimeClassification: Extract Begin and Date for each Ticket from SQL. Then use it to calculate the duration of each one and then classification then into 4 categories. Then, extract mapping from sql linking each message to a ticket id, its duration and classification.

6. Pos-process: Join all the generated files in two csv compiled files. The first one contains full information, with clear and translated body, scores and classifications. The second contains only the ids related and final classfications.