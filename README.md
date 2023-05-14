# Whisper for Sociolinguistics

This is a repository for the [code](/Whisper.py) that uses OpenAI’s [Whisper](https://github.com/openai/whisper) to automatically transcribe interviews obtained for the sociolinguistics project EMILS-ISMX (Experiencias Migratorias: Identidad, Lengua y Sociedad. Integración Sociolingüística en México) developed by Ph.D. candidate [Brenda Berenice Larios Loza](https://upol.academia.edu/BrendaBereniceLariosLoza) (Palacký University Olomouc and University of Granada, [ResearchGate](https://www.researchgate.net/profile/Brenda-Larios-Loza)).

### About the project EMILS-ISMX

The aim of the project EMILS-ISMX is to study the sociolinguistic integration of Central American and Caribbean migrants in Mexico. In the recent years, a significant number of irregular migrants have been transiting from the South to the North of the American continent. The main reason is the desire to improve their quality of life. In other words, the migrants wish to escape poverty, violence, organized crime as well as other difficult aspects of their lives. Mexico is an important location in their journey since it is the interregional border between the two Americas and each year it receives thousands of migrants (for statistics see Unidad de Política Migratoria).[^1] In this scenery, linguistic factors play a crucial role. Even though the migrants usually have Spanish as their mother tongue, there is a difference between their variety of Spanish and the variety spoken in Mexico. Consequently, they may face linguistic and communicative challenges during their journey.

### Interviews

To investigate the sociolinguistic integration of the migrants and their attitudes towards the Mexican Spanish, Brenda Berenice Larios Loza conducted 128 semi-structured interviews with migrants staying in 6 different migrant houses ([see the map](https://www.google.com/maps/d/u/1/viewer?mid=1EcMXcebgV9G5DGapAfiswYlEc-5gvZA&ll=25.93618304769706%2C-97.55053775275245&z=6)). Those interviews have a duration between 20 and 40 minutes, with some exceptions with more than 60 minutes. In total, the duration of the audios is 55 hours, 48 minutes, 12 seconds. Transcribe such quantity of interviews in a limited time frame and as a sole researcher manually is nearly impossible. Also, the quality of audios is not always very high, because the interviews were usually conducted in common areas of the migrant houses, so background noise and other voices can be heard in them. Because of that, the tools such as MS Word dictator did not deliver great results. Other possible aspect that could difficult the automatic transcription is the fact that in each audio, there are two participants speaking one language (Spanish), but two different varieties of this language. Moreover, participants use colloquial and regional vocabulary, differ in volume of their voice, etc.

Thus, the main challenges for transcription are:

-	More that 55 hours of audio
-	Background noises, interruptions
-	Contact of different varieties of Spanish in each audio
-	Colloquial, regional vocabulary
-	Volume of speakers’ voices

When in September of 2022 the OpenAI’s speech recognition model named Whisper was released to public, we decided to try it for automatic transcription of the interviews and see the quality of results. The big advantage of Whisper for this case was the fact that the WER (Word Error Rate) for Spanish is the lowest of all languages (only 3.0) and that the language model was trained with a large dataset that includes diverse audios in different qualities and registers of speech.[^2]

To automatically transcribe all the interviews, we used the large multilingual model, because we were interested to achieve the best possible quality of transcription. We then used a [python code](/Whisper.py) to transcribe automatically all the audio files with interviews stored in one folder and save the outcome as a .txt file with the same name as the name of its respective audio file.

### Results

The quality of resulting transcriptions was very good, and it saved us plenty of time that would otherwise be needed to transcribe the audios manually. Still, the transcriptions needed to be manually corrected. After the corrections, we identified following common types of errors:

-	Local toponymy
-	Indigenous vocabulary
-	Lexical borrowings
-	Dates
-	Some pronunciation/phonetics related errors

Surprisingly, there were no noticeable differences in quality for different varieties of Spanish. Neither the pronunciation (*seseo*) affected the transcription negatively. The factors that affected the quality the most are related to acoustics: audio quality and volume of voice.

### Final remarks

In conclusion, Whisper proved to be a useful tool that can facilitate the labor of transcribing audio, in this case, sociolinguistic interviews. It is relatively easy to use and, even though a manual correction is necessary, for Spanish, it delivers good quality transcriptions in short time.

### Publications of the project EMILS-ISMX

[to be added]


[^1]: Unidad de política migratoria de México (2022): Estadísticas migratorias, enero-noviembre
de 2022. Retrieved from: Mapa de estadísticas básicas, Gobierno de México:
http://portales.segob.gob.mx/es/PoliticaMigratoria/Mapa_estadisticas/?Mapa=2022

[^2]: Radford Alec, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey and Ilya Sutskever (2022): “Robust Speech Recognition via Large-Scale Weak Supervision” in arXiv preprint arXiv: 2212.04356, doi: https://doi.org/10.48550/arXiv.2212.04356.
