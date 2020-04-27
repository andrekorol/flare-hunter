const chalk = require('chalk');

// define styles for console.log
module.exports = {
  warning: chalk.keyword('orange'),
  error: chalk.bold.red,
  success: chalk.green,
  info: chalk.blue.bold,
};
