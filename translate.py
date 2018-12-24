var phrases1 = []
var phrases2 = []
var words1 = ["me","love","fuck"]
var words2 = ["me","wuv","nnya"]
var intraword1 = ["ll","l","r"]
var intraword2 = ["ww","w","w"]
var prefixes1 = ["l","r","m"]
var prefixes2 = ["w","w","mw"]
var suffixes1 = ["ll","er","l","r","!","?"][
var suffixes2 = ["ww","ah","w","w","!!","??"]
var regex1 = "\/[!]$\/g\n\/[?.]$\/g"
var regex2 = "$' OwO\n$' UwU\n"
var rev_regex1 = []
var rev_regex2 = []
var ordering1 = []
var ordering2 = []
 

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



