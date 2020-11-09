const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");

module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy('static');
    eleventyConfig.addPlugin(syntaxHighlight);
    eleventyConfig.addCollection("poemsDesc", (collection) =>
      collection.getFilteredByGlob("content/poems/*.md").filter(item => !['index'].includes(item.tags)).sort((a, b) => {
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