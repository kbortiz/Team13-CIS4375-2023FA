export const pieChartData = {
  type: "pie",
  data: {
    //instead of zip codes I will leave it by areas, I know the requirements
    //wanted zipcodes but this looks better and for the backend I will bind zip codes
    //to areas. Since one Houston area can have multiple zip codes, this makes sense to me.
    labels: [
      'Memorial',
      'Galleria',
      'Westchase',
      'Humble',
      'Spring'
    ],
    datasets: [{
      label: 'Quantity',
      // Number of events per area
      data: [7, 5, 13, 9, 5],
      backgroundColor: [
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)',
        'rgb(20, 22, 236)',
        'rgb(22, 236, 20)',
        'rgb(0, 85, 18)'
      ]
    }]
  },
  options: {
    responsive: true,
    lineTension: 1,
      width: 200,
      height: 200
  }
};
export default pieChartData;