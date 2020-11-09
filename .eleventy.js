const syntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");

module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy('static');
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