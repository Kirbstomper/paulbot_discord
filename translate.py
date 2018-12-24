var phrases1 = new Array();
var phrases2 = new Array();
var words1 = new Array();
var words2 = new Array();
var intraword1 = new Array();
var intraword2 = new Array();
var prefixes1 = new Array();
var prefixes2 = new Array();
var suffixes1 = new Array();
var suffixes2 = new Array();
var regex1 = new Array();
var regex2 = new Array();
var rev_regex1 = new Array();
var rev_regex2 = new Array();
var ordering1 = new Array();
var ordering2 = new Array();
function numRules() {
    return phrases1.length + phrases2.length + words1.length + words2.length + intraword1.length + intraword2.length + prefixes1.length + prefixes2.length + suffixes1.length + suffixes2.length + regex1.length + regex2.length + rev_regex1.length + rev_regex2.length + ordering1.length + ordering2.length;
}
var doneToken = "����}�";
var sentenceCount = 0;
var useWebWorker = false;
function translate(text, direction) {
    if (direction === "backward" && reverseIsDisabled)
        return $("#english-text").val();
    if (useWebWorker || ((typeof forward !== "function") && numRules() > 1000)) {
        translateWithWebWorker(text, direction);
        return;
    }
    if (text == "")
        return "";
    var translatedText = "";
    if (!([].concat(phrases1, phrases2, words1, words2, intraword1, intraword2, prefixes1, prefixes2, suffixes1, suffixes2, regex1, regex2, rev_regex1, rev_regex2, ordering1, ordering2).join("").length === 0)) {
        sentenceCount = 0;
        sentenceArray = text.split(/(\.)/g);
        sentenceArray = sentenceArray.filter(function(s) {
            return s !== "";
        })
        for (var i = 0; i < sentenceArray.length; i++) {
            text = sentenceArray[i];
            if (text === ".") {
                translatedText += ".";
                continue;
            }
            if (text.trim() === "") {
                translatedText += text;
                continue;
            }
            var startsWithSpace = false;
            if (text[0] === " ") {
                startsWithSpace = true;
            }
            var firstLetterIsCapital = false;
            if (text.trim()[0] === text.trim()[0].toUpperCase()) {
                firstLetterIsCapital = true;
            }
            if (direction == "backward") {
                text = intrawordSwap(intraword2, intraword1, text);
                text = " " + text + " ";
                text = text.toLowerCase();
                text = text.split("\n").join(" 985865568NEWLINETOKEN98758659 ");
                text = phraseSwap(phrases2, phrases1, text);
                text = wordSwap(words2, words1, text);
                text = prefixSwap(prefixes2, prefixes1, text);
                text = suffixSwap(suffixes2, suffixes1, text);
                text = removeDoneTokens(text);
                text = text.split(doneToken).join("");
                text = text.trim();
                text = regexReplace(rev_regex1, rev_regex2, text);
                text = wordOrdering(ordering2, ordering1, text);
            } else {
                text = intrawordSwap(intraword1, intraword2, text);
                text = " " + text + " ";
                text = text.toLowerCase();
                text = text.split("\n").join(" 985865568NEWLINETOKEN98758659 ");
                text = phraseSwap(phrases1, phrases2, text);
                text = wordSwap(words1, words2, text);
                text = prefixSwap(prefixes1, prefixes2, text);
                text = suffixSwap(suffixes1, suffixes2, text);
                text = removeDoneTokens(text);
                text = text.split(doneToken).join("");
                text = text.trim();
                text = regexReplace(regex1, regex2, text);
                text = wordOrdering(ordering1, ordering2, text);
            }
            text = text.split(" 985865568NEWLINETOKEN98758659 ").join("\n");
            text = text.split(" 985865568NEWLINETOKEN98758659").join("\n");
            text = text.split("985865568NEWLINETOKEN98758659").join("\n");
            text = text.replace(/(\b\S+\b)[ ]+\b\1\b/gi, "$1 $1");
            if (firstLetterIsCapital) {
                text = text[0].toUpperCase() + text.substr(1);
            }
            if (startsWithSpace) {
                text = " " + text;
            }
            translatedText += text;
            sentenceCount++;
        }
        translatedText = translatedText.split('{{*DUPLICATE MARKER*}}').join('');
        if (typeof doApplySentenceCase !== 'undefined') {
            if (doApplySentenceCase !== false) {
                translatedText = applySentenceCase(translatedText);
                translatedText = capitalizeFirstLetter(translatedText);
            }
        }
    } else {
        translatedText = text;
    }
    if (direction == "backward" && typeof backward === "function") {
        translatedText = backward(translatedText);
    } else if (typeof forward === "function") {
        translatedText = forward(translatedText);
    }
    return translatedText;
}


#usage
var jsonData = {
                    "phrases1": "",
                    "phrases2": "",
                    "words1": "me\nlove\nfuck",
                    "words2": "me\nwuv\nnya",
                    "intraword1": "ll\nl\nr",
                    "intraword2": "ww\nw\nw",
                    "prefixes1": "l\nr\nm",
                    "prefixes2": "w\nw\nmw",
                    "suffixes1": "ll\ner\nl\nr\n!\n?",
                    "suffixes2": "ww\nah\nw\nw\n!!\n??",
                    "regex1": "\/[!]$\/g\n\/[?.]$\/g",
                    "regex2": "$' OwO\n$' UwU\n",
                    "rev_regex1": "",
                    "rev_regex2": "",
                    "ordering1": "",
                    "ordering2": ""
                };
                phrases1 = jsonData.phrases1.split("\n");
                phrases2 = jsonData.phrases2.split("\n");
                words1 = jsonData.words1.split("\n");
                words2 = jsonData.words2.split("\n");
                intraword1 = jsonData.intraword1.split("\n");
                intraword2 = jsonData.intraword2.split("\n");
                prefixes1 = jsonData.prefixes1.split("\n");
                prefixes2 = jsonData.prefixes2.split("\n");
                suffixes1 = jsonData.suffixes1.split("\n");
                suffixes2 = jsonData.suffixes2.split("\n");
                regex1 = jsonData.regex1.split("\n");
                regex2 = jsonData.regex2.split("\n");
                rev_regex1 = jsonData.rev_regex1.split("\n");
                rev_regex2 = jsonData.rev_regex2.split("\n");
                ordering1 = jsonData.ordering1.split("\n");
                ordering2 = jsonData.ordering2.split("\n");
