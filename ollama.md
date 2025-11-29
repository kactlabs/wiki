/ [Home](index.md)

## Ollama

**Note:** tbw


```
curl -fsSL https://ollama.com/install.sh | sh


ollama --version
ollama version is 0.3.3
2024-12-28 07:48:24


https://ollama.com/download/mac

brew install ollama




ollama --version
Warning: could not connect to a running Ollama instance
Warning: client version is 0.5.4
2024-12-28 08:02:07


ollama version is 0.5.7



ollama serve

OLLAMA_DEBUG=true ollama serve


http://localhost:11434/

http://localhost:11434/v1


ollama pull llama3


```



```
curl http://localhost:11434
Ollama is running%
```




```
ollama show qwen3:0.6b
  Model
    architecture        qwen3
    parameters          751.63M
    context length      40960
    embedding length    1024
    quantization        Q4_K_M

  Capabilities
    completion
    tools
    thinking

  Parameters
    top_p             0.95
    repeat_penalty    1
    stop              "<|im_start|>"
    stop              "<|im_end|>"
    temperature       0.6
    top_k             20

  License
    Apache License
    Version 2.0, January 2004
    ...
```



```
ollama show qwen3:0.6b --license
```


```
ollama show orca-mini --modelfile
```


```
ollama run mistral --verbose "Please can you summarise this article: $(cat casteism.txt)"

 The Manusmriti, an ancient Indian text regarded as the most authoritative on Hindu law, endorses and justifies the caste system as essential for societal order and regularity. The caste system consists of
four main groups: Brahmins (priests and intellectuals), Kshatriyas (warriors and rulers), Vaishyas (traders), and Shudras (workers). These groups are believed to have originated from different parts of the
Hindu God of creation, Brahma.

The caste system is further divided into around 3,000 castes and 25,000 sub-castes based on specific occupations. Below this hierarchy are the achhoots (Dalits or untouchables) who were excluded from the
caste system.

Throughout history, caste has significantly influenced Hindu religious and social life, with each group having a specific place in the social hierarchy. Upper castes enjoyed privileges while repressing lower
castes. The rigid caste system, often criticized for its unjustness and regressiveness, remained largely unchanged for centuries, trapping individuals within fixed social orders.

Despite the challenges, notable figures like BR Ambedkar (author of the Indian Constitution) and KR Narayanan (first Dalit president of India) have risen to prominent positions in the country. Historians
suggest that prior to the 18th century, caste distinctions were less formal, and social identities were more fluid with individuals able to move between castes easily.

The British colonial rulers are believed to have solidified the caste system by using censuses to simplify it, making it India's defining social feature for easier governance.

total duration:       9.881429042s
load duration:        2.133380792s
prompt eval count:    645 token(s)
prompt eval duration: 1.050608542s
prompt eval rate:     613.93 tokens/s
eval count:           379 token(s)
eval duration:        6.6954475s
eval rate:            56.61 tokens/s
```


```
ollama run mistral --verbose "If you had to categorise this article, what tags would you use?: $(cat casteism.txt)"
 Here are some potential tags for this article:

1. Hinduism
2. Caste System
3. Manusmriti
4. Indian History
5. Social Structure
6. Brahmin, Kshatriya, Vaishya, Shudra
7. Dalits (Untouchables)
8. Social Inequality
9. British Colonial Rule
10. BR Ambedkar
11. KR Narayanan
12. Indian Constitution
13. Caste-based Discrimination
14. Social Mobility
15. Social Hierarchy
16. Religious and Social Life in India
17. Traditional Indian Society
18. Social Reform Movements
19. Colonial Influence on Indian Society
20. Caste Census

total duration:       4.226764291s
load duration:        6.458333ms
prompt eval count:    652 token(s)
prompt eval duration: 1.021289417s
prompt eval rate:     638.41 tokens/s
eval count:           182 token(s)
eval duration:        3.198590208s
eval rate:            56.90 tokens/s
```



```
 curl -X POST http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "What is the sentiment of this sentence: The situation surrounding the video assistant referee is at crisis point."
}'
{"model":"mistral","created_at":"2025-11-19T03:55:58.447573Z","response":" The","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.46301Z","response":" sentiment","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.478995Z","response":" of","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.494731Z","response":" the","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.510854Z","response":" sentence","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.526076Z","response":" \"","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.542257Z","response":"The","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.557477Z","response":" situation","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.573717Z","response":" surrounding","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.58899Z","response":" the","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.605253Z","response":" video","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.620774Z","response":" assistant","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.637101Z","response":" ref","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.6535Z","response":"eree","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.669499Z","response":" is","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.685853Z","response":" at","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.701567Z","response":" crisis","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.717793Z","response":" point","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.733097Z","response":"\"","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.749221Z","response":" is","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.764735Z","response":" negative","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.781571Z","response":".","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.797086Z","response":" This","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.814288Z","response":" implies","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.830755Z","response":" that","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.846903Z","response":" there","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.864372Z","response":"'","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.880518Z","response":"s","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.896644Z","response":" a","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.912546Z","response":" serious","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.928345Z","response":" problem","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.945175Z","response":" or","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.961375Z","response":" urgent","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.977675Z","response":" need","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:58.994086Z","response":" for","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.010498Z","response":" resolution","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.027081Z","response":" regarding","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.04386Z","response":" the","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.059877Z","response":" video","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.076579Z","response":" assistant","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.092471Z","response":" ref","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.10939Z","response":"eree","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.125222Z","response":".","done":false}
{"model":"mistral","created_at":"2025-11-19T03:55:59.141608Z","response":"","done":true,"done_reason":"stop","context":[3,29473,2592,1117,1040,22558,1070,1224,13039,29515,1183,5388,12796,1040,4566,14660,2560,15215,1117,1206,11556,2073,29491,4,29473,1183,22558,1070,1040,13039,1113,1782,5388,12796,1040,4566,14660,2560,15215,1117,1206,11556,2073,29507,1117,7855,29491,1619,12918,1137,1504,29510,29481,1032,5360,3468,1210,26744,1695,1122,11716,8985,1040,4566,14660,2560,15215,29491],"total_duration":777193209,"load_duration":8619292,"prompt_eval_count":25,"prompt_eval_duration":73714625,"eval_count":44,"eval_duration":694381250}
```


```
ollama show --modelfile llama2:latest
```


```
ollama rm llama2:latest
```


```
https://tamilsonglyrics4u.com/sangeetha-megam-lyrics-udhaya-geetham-1985.html


ollama run orca-mini --verbose "Please can you summarise this lyrics in 3 lines: $(cat sangeetha-megam-english.txt)"  

The lyrics are about the beauty and power of music, and the speaker's determination to keep creating it despite the challenges they may face. They suggest that music is a powerful force that can 
overcome obstacles and bring joy to people's lives. The lyrics also emphasize the importance of perseverance and staying true to one's art.

total duration:       11.51944286s
load duration:        147.379µs
prompt eval count:    992 token(s)
prompt eval duration: 3.513464s
prompt eval rate:     282.34 tokens/s
eval count:           68 token(s)
eval duration:        8.005424s
eval rate:            8.49 tokens/s
```




```
https://tamilsonglyrics4u.com/sangeetha-megam-lyrics-udhaya-geetham-1985.html
https://www.tamil2lyrics.com/lyrics/sangeetha-megam-song-lyrics/

ollama run orca-mini --verbose "Please can you summarise this lyrics in 3 lines: $(cat sangeetha-megam-english.txt)"  

The lyrics are about the beauty and power of music, and the speaker's determination to keep creating it despite the challenges they may face. They suggest that music is a powerful force that can 
overcome obstacles and bring joy to people's lives. The lyrics also emphasize the importance of perseverance and staying true to one's art.

total duration:       11.51944286s
load duration:        147.379µs
prompt eval count:    992 token(s)
prompt eval duration: 3.513464s
prompt eval rate:     282.34 tokens/s
eval count:           68 token(s)
eval duration:        8.005424s
eval rate:            8.49 tokens/s
```



```
ollama run mistral --verbose "Please can you summarise this lyrics in 3 lines: $(cat sangeetha-megam-english.txt)"
 This Tamil song has a recurring chorus with the lines "Sangeetha megam thaen sindhum neram" and "Aagaayam pookal thoovum kaalam." The male singer expresses longing for the beauty of music (sangeetha) like
the ocean (sindhu), and the female responds with repetitive "lala" sounds.

The lyrics also describe a deep connection between the singer and the music, expressing that life without it is empty ("Naazhai en geedhamae engum ulaavumae"). The singer mentions the power of music to bring
joy ("Jeeva sugam pera raaga nadhiyinil nee neendhavaa") and its ability to define a unique path ("Indha thegam maraindhaalum isaiyaai malarven").

The song also speaks of the deep bond between the singer and music, depicting their unity as inseparable ("Ullam ennum oorilae paadal ennum therilae") and expresses a desire for that connection to never end
("Endhan moochum indha paatum anaiyaa vilakae"). The song concludes by repeating the chorus once more.

total duration:       6.585765416s
load duration:        1.084616375s
prompt eval count:    471 token(s)
prompt eval duration: 756.507209ms
prompt eval rate:     622.60 tokens/s
eval count:           277 token(s)
eval duration:        4.74293525s
eval rate:            58.40 tokens/s
```



```
ollama run mistral --verbose "Please can you summarise this lyrics in 3 lines: $(cat sangeetha-megam-english.txt)"
 This Tamil song has a recurring chorus with the lines "Sangeetha megam thaen sindhum neram" and "Aagaayam pookal thoovum kaalam." The male singer expresses longing for the beauty of music (sangeetha) like
the ocean (sindhu), and the female responds with repetitive "lala" sounds.

The lyrics also describe a deep connection between the singer and the music, expressing that life without it is empty ("Naazhai en geedhamae engum ulaavumae"). The singer mentions the power of music to bring
joy ("Jeeva sugam pera raaga nadhiyinil nee neendhavaa") and its ability to define a unique path ("Indha thegam maraindhaalum isaiyaai malarven").

The song also speaks of the deep bond between the singer and music, depicting their unity as inseparable ("Ullam ennum oorilae paadal ennum therilae") and expresses a desire for that connection to never end
("Endhan moochum indha paatum anaiyaa vilakae"). The song concludes by repeating the chorus once more.

total duration:       6.585765416s
load duration:        1.084616375s
prompt eval count:    471 token(s)
prompt eval duration: 756.507209ms
prompt eval rate:     622.60 tokens/s
eval count:           277 token(s)
eval duration:        4.74293525s
eval rate:            58.40 tokens/s


```


```
ollama run mistral --verbose "Please can you summarise this lyrics in 3 lines: $(cat sangeetha-megam-english.txt)"

 This Tamil song has a repeated chorus of "Sangeetha megam thaen sindhum neram, Aagaayam pookal thoovum kaalam," which translates to "The ocean is music's majesty, the sunrise are blooming flowers in time."
The lyrics express a longing for a love that transcends time and space. The female part consists of repeated "lala" sounds, while the male parts include lines about the heart yearning for its beloved and the
beauty of life's rhythm. The chorus returns with references to music's grandeur and the sunrise as blooming flowers in time, suggesting an ongoing appreciation for both music and love.

total duration:       2.53989325s
load duration:        7.214458ms
prompt eval count:    471 token(s)
prompt eval duration: 22.657584ms
prompt eval rate:     20787.74 tokens/s
eval count:           149 token(s)
eval duration:        2.509575791s
eval rate:            59.37 tokens/s
```



```
ollama run orca-mini --verbose "Can you pull out 5 bullet points from the following article: $(cat sangeetha-megam-english.txt)"
 Sure! Here are the 5 bullet points from the article:

1. Male: "Sangeetha megam thaen sindhum neram" (I have a lot of memories)
2. Male: "Aagaayam pookal thoovum kaalam" (The world is full of experiences)
3. Male: "Naazhai en geedhamae engum ulaavumae" (We all have different paths in life)
4. Male: "Endrum vizhavae en vaazhvilae … ae … ooh oh" (But we all have the same desire to make our lives meaningful)
5. Female: "Lala lala lala lala laa" (It's like a long and winding road)

Female: "Lala lala laa" (It's like a long and winding road)


total duration:       2.326923416s
load duration:        7.621666ms
prompt eval count:    511 token(s)
prompt eval duration: 453.155917ms
prompt eval rate:     1127.65 tokens/s
eval count:           200 token(s)
eval duration:        1.865716792s
eval rate:            107.20 tokens/s
```



```
ollama run mistral --verbose "What's the sentiment of this article: $(cat sangeetha-megam-english.txt)"

 The article appears to contain lyrics from a Tamil song, and it's difficult to determine an overall sentiment based solely on the lyrics provided. However, some phrases suggest longing or yearning, such as
"Naazhai en geedhamae engum ulaavumae" (There is no comfort for me anywhere) and "Endrum vizhavae en vaazhvilae" (I am searching everywhere for you). Additionally, the repetition of phrases like "Sangeetha
megam thaen sindhum neram" (The splendor of music in the ocean), "Aagaayam pookal thoovum kaalam" (A thousand blossoms blooming at once), and "Kelaai poo manamae ... ooh oh" could be interpreted as expressing
deep emotion or passion for the subject. Overall, the lyrics seem to evoke feelings of longing, yearning, and possibly love or admiration.

total duration:       4.330319792s
load duration:        6.78775ms
prompt eval count:    468 token(s)
prompt eval duration: 723.854042ms
prompt eval rate:     646.54 tokens/s
eval count:           207 token(s)
eval duration:        3.599059916s
eval rate:            57.52 tokens/s
```



```
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "What is the sentiment of this sentence: The situation surrounding the video assistant referee is at crisis point."
 }'
{"model":"mistral","created_at":"2025-11-19T04:06:09.777576Z","response":" The","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.793931Z","response":" sentiment","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.809771Z","response":" of","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.825532Z","response":" the","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.841428Z","response":" sentence","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.857096Z","response":" \"","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.872869Z","response":"The","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.888619Z","response":" situation","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.905086Z","response":" surrounding","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.920526Z","response":" the","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.936371Z","response":" video","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.952326Z","response":" assistant","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.968323Z","response":" ref","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.983961Z","response":"eree","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:09.999828Z","response":" is","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.01569Z","response":" at","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.03174Z","response":" crisis","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.048056Z","response":" point","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.064089Z","response":"\"","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.080029Z","response":" is","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.096459Z","response":" negative","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.112376Z","response":",","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.128213Z","response":" as","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.143524Z","response":" it","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.15955Z","response":" implies","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.175531Z","response":" a","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.191449Z","response":" serious","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.207541Z","response":" and","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.224904Z","response":" critical","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.242262Z","response":" state","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.25926Z","response":" or","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.274988Z","response":" problem","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.291435Z","response":" with","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.307163Z","response":" the","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.323371Z","response":" video","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.338866Z","response":" assistant","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.355117Z","response":" ref","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.370535Z","response":"eree","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.386391Z","response":" system","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.40231Z","response":".","done":false}
{"model":"mistral","created_at":"2025-11-19T04:06:10.41834Z","response":"","done":true,"done_reason":"stop","context":[3,29473,2592,1117,1040,22558,1070,1224,13039,29515,1183,5388,12796,1040,4566,14660,2560,15215,1117,1206,11556,2073,29491,4,29473,1183,22558,1070,1040,13039,1113,1782,5388,12796,1040,4566,14660,2560,15215,1117,1206,11556,2073,29507,1117,7855,29493,1158,1146,12918,1032,5360,1072,8044,2433,1210,3468,1163,1040,4566,14660,2560,15215,2355,29491],"total_duration":726229375,"load_duration":9582459,"prompt_eval_count":25,"prompt_eval_duration":75168792,"eval_count":41,"eval_duration":640964875}
```




```
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "orca-mini",
  "prompt": "What is the sentiment of this sentence: The situation surrounding the video assistant referee is at crisis point."
 }'
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.363286Z","response":" The","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.371758Z","response":" sentiment","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.380295Z","response":" of","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.388453Z","response":" the","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.396592Z","response":" sentence","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.404855Z","response":" is","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.413635Z","response":" negative","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.422462Z","response":"/","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.431309Z","response":"s","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.439876Z","response":"ke","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.447779Z","response":"pt","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.455995Z","response":"ical","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.464206Z","response":".","done":false}
{"model":"orca-mini","created_at":"2025-11-19T04:06:31.472387Z","response":"","done":true,"done_reason":"stop","context":[31822,13,8458,31922,3244,31871,13,3838,397,363,7421,8825,342,5243,10389,5164,828,31843,9530,362,988,362,365,473,31843,13,13,8458,31922,9779,31871,13,5449,322,266,17324,287,433,7966,31871,347,3415,7011,266,2344,8825,30571,322,389,4907,1119,31843,13,13,8458,31922,13166,31871,13,347,17324,287,266,7966,322,5569,31873,31829,401,451,489,31843],"total_duration":177109500,"load_duration":8078500,"prompt_eval_count":60,"prompt_eval_duration":59284209,"eval_count":14,"eval_duration":109362041}
```




```
how to delete all models in ollama

ollama list | awk 'NR>1 {print $1}' | xargs -n 1 ollama rm
```



```
Delete one by one:

ollama rm tinyllama
ollama rm phi
ollama rm gemma:2b
```


### How to publish to Ollama?
```
ollama create rajacsp/kollywood-expert:v7.0.4 -f Modelfile.v7.0.4

ollama push rajacsp/kollywood-expert:v7.0.4

ollama cp rajacsp/kollywood-expert:v7.0.4 rajacsp/kollywood-expert:latest

ollama push rajacsp/kollywood-expert:latest
```