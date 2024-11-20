function wordCount(val) {
    let wom = val.match(/\S+/g);
    return {
        charactersNoSpace : val.replace(/\s+/g, '').length,
        characters : val.length,
        words : wom ? wom.length : 0,
        lines : val.split(/\r*\n/).length
    };
}

console.log(wordCount("someMultilineText").words);