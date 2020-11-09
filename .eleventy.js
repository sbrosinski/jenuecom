const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");

module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy('css');
    eleventyConfig.addPassthroughCopy('img');
    eleventyConfig.addPlugin(syntaxHighlight);
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