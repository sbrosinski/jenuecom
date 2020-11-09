const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");

module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy('static');
    eleventyConfig.addPassthroughCopy('CNAME');
    eleventyConfig.addPlugin(syntaxHighlight);
    eleventyConfig.addCollection("poemsAsc", (collection) =>
      collection.getFilteredByTags("poem").sort((a, b) => {
        if (a.data.title > b.data.title) return 1;
        else if (a.data.title < b.data.title) return -1;
        else return 0;
        })
    );
    eleventyConfig.addCollection("shortAsc", (collection) =>
      collection.getFilteredByTags("short").sort((a, b) => {
        if (a.data.title > b.data.title) return 1;
        else if (a.data.title < b.data.title) return -1;
        else return 0;
        })
    );
    eleventyConfig.addCollection("novelsAsc", (collection) =>
      collection.getFilteredByTags("novel").sort((a, b) => {
        if (a.data.title > b.data.title) return 1;
        else if (a.data.title < b.data.title) return -1;
        else return 0;
        })
    );
    return {
      passthroughFileCopy: true,
      dir: {
        input: 'content',
        includes: '_includes',
        data: '_data',
        output: 'docs',
      },
    }
  }