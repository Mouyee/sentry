/**
 * Top Errors by Device
 */
const topDevices = {
  name: 'Top Devices',
  fields: ['device.family'],
  conditions: [],
  aggregations: [['count()', null, 'count']],
  limit: 10,

  orderby: '-count',
  groupby: ['device.family'],
};

export default topDevices;
