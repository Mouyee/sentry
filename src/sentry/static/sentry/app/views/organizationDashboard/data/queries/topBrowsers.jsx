/**
 * Top Errors by Browser
 */
const topBrowsers = {
  name: 'Top Browsers',
  fields: ['browser.name'],
  conditions: [],
  aggregations: [['count()', null, 'count']],
  limit: 10,

  orderby: '-count',
  groupby: ['browser.name'],
};

export default topBrowsers;
