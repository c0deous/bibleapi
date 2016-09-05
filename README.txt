This is an api written in python that returns verses out of the King James bible.  It uses bottle as the engine.
By default it runs on port 5934 but you can change this in the bibleapi file.
-------------------------------------------------------------------------------
USAGE:
Single Verse: address:port/bookid/chapter/verse1/[verse2]

2 verses from the same chapter and book: address:port/bookid/chapter/verse1/verse2

Information: address:port/info

NOTE: The bookid is the index number of the bible book where genesis would be 1 and exodus would
NOTE: be 2, leviticus 3 and so on...

List of all of the books and their number:
1	Genesis		40	Matthew
2	Exodus		41	Mark
3	Leviticus	42	Luke
4	Numbers		43	John
5	Deuteronomy	44	Acts
6	Joshua		45	Romans
7	Judges		46	1 Corinthians
8	Ruth		47	2 Corinthians
9	1 Samuel	48	Galatians
10	2 Samuel	49	Ephesians
11	1 Kings		50	Philippians
12	2 Kings		51	Colossians
13	1 Chronicles	52	1 Thessalonians
14	2 Chronicles	53	2 Thessalonians
15	Ezra		54	1 Timothy
16	Nehemiah	55	2 Timothy
17	Esther		56	Titus
18	Job		57	Philemon
19	Psalms		58	Hebrews
20	Proverbs	59	James
21	Ecclesiastes	60	1 Peter
22	Solomon		61	2 Peter
23	Isaiah		62	1 John
24	Jeremiah	63	2 John
25	Lamentations	64	3 John
26	Ezekiel		65	Jude
27	Daniel		66	Revelation
28	Hosea
29	Joel
30	Amos
31	Obadiah
32	Jonah
33	Micah
34	Nahum
35	Habakkuk
36	Zephaniah
37	Haggai
38	Zechariah
39	Malachi

-------------------------------------------------------------------------------
This project by Jesse Wallace (c0deous) <c0deo.us>
