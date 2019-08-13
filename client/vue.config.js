require("dotenv").config();

const path = require("path"),
  outputDir = path.resolve(__dirname, "../", process.env.BUILD_TEMPLATE_DIR),
  assetsDir = path.relative(outputDir, process.env.BUILD_ASSET_DIR);
  
module.exports = {
  assetsDir,
  publicPath: "",
  outputDir,
};
