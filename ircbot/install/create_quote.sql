/**
 * sqlite3 db/pm.db < install/create_quote.sql
 */
DROP TABLE yoda_en;
CREATE TABLE yoda_en (id INTEGER PRIMARY KEY, quote VARCHAR);

INSERT INTO yoda_en (quote) VALUES("Agree with you, the council does. Your apprentice, Skywalker will be.");
INSERT INTO yoda_en (quote) VALUES("Always two there are, no more, no less: a master and an apprentice.");
INSERT INTO yoda_en (quote) VALUES("Fear is the path to the Dark Side. Fear leads to anger, anger leads to hate; hate leads to suffering. I sense much fear in you.");
INSERT INTO yoda_en (quote) VALUES("Qui-Gon's defiance I sense in you.");
INSERT INTO yoda_en (quote) VALUES("Truly wonderful the mind of a child is.");
INSERT INTO yoda_en (quote) VALUES("Around the survivors a perimeter create.");
INSERT INTO yoda_en (quote) VALUES("Lost a planet Master Obi-Wan has. How embarrassing ... how embarrassing.");
INSERT INTO yoda_en (quote) VALUES("Victory, you say? Master Obi-Wan, not victory. The shroud of the Dark Side has fallen. Begun the Clone War has.");
INSERT INTO yoda_en (quote) VALUES("Much to learn you still have ... my old padawan. ... This is just the beginning!");
INSERT INTO yoda_en (quote) VALUES("Twisted by the Dark Side young Skywalker has become.");
INSERT INTO yoda_en (quote) VALUES("The boy you trained, gone he is, consumed by Darth Vader.");
INSERT INTO yoda_en (quote) VALUES("Death is a natural part of life. Rejoice for those around you who transform into the Force. Mourn them do not. Miss them do not. Attachment leads to jealousy. The shadow of greed that is . Train yourself to let go of everything you fear to lose.");
INSERT INTO yoda_en (quote) VALUES("The fear of loss is a path to the Dark Side.");
INSERT INTO yoda_en (quote) VALUES("If into the security recordings you go, only pain will you find.");
INSERT INTO yoda_en (quote) VALUES("Not if anything to say about it I have.");
INSERT INTO yoda_en (quote) VALUES("Great warrior, hmm? Wars not make one great.");
INSERT INTO yoda_en (quote) VALUES("Do or do not; there is no try.");
INSERT INTO yoda_en (quote) VALUES("Size matters not. Look at me. Judge me by my size, do you?");
INSERT INTO yoda_en (quote) VALUES("That is why you fail.");
INSERT INTO yoda_en (quote) VALUES("No! No different. Only different in your mind. You must unlearn what you have learned.");
INSERT INTO yoda_en (quote) VALUES("Always in motion the future is.");
INSERT INTO yoda_en (quote) VALUES("Reckless he is. Matters are worse.");
INSERT INTO yoda_en (quote) VALUES("No. There is another. ...");
INSERT INTO yoda_en (quote) VALUES("When nine hundred years old you reach, look as good, you will not.");
INSERT INTO yoda_en (quote) VALUES("There is ... another ... Sky ... walker. ...");
INSERT INTO yoda_en (quote) VALUES("When 900 years old you reach, look as good you will not ehh.");

SELECT * FROM yoda_en;

DROP TABLE yoda_de;
CREATE TABLE yoda_de(id INTEGER PRIMARY KEY, quote VARCHAR);

INSERT INTO yoda_de (quote) VALUES("Immer zwei es sind! Ein Schüler und ein Meister!");
INSERT INTO yoda_de (quote) VALUES("... Luke, Luke, wenn diese Welt ich verlassen habe , der letzte der Jedi wirst Du sein.");
INSERT INTO yoda_de (quote) VALUES("Du darfst niemals vergessen: Deine Wahrnehmung bestimmt deine Realität!");
INSERT INTO yoda_de (quote) VALUES("Ist die dunkle Seite stärker? - Nein. Nein... nein. Schneller, leichter, verführerischer.");
INSERT INTO yoda_de (quote) VALUES("Schwer zu sehen, in ständiger Bewegung die Zukunft ist.");
INSERT INTO yoda_de (quote) VALUES("Vergessen du musst was früher du gelernt.");
INSERT INTO yoda_de (quote) VALUES("Du kannst Veränderungen nicht aufhalten. Genau so wie du die Sonne nicht daran hindern kannst unterzugehen.");

SELECT * FROM yoda_de;
