function generateTable() {
  var data = score_table; // The variable from model_scores.js

  var table = '';
  table += `<tr>
          <td class="js-sort-number"><strong>#</strong></td>
          <td class="js-sort-number"><strong>Model</strong></td>
          <td class="js-sort-number"><strong>Method</strong></td>
          <td class="js-sort-number"><strong>Source</strong></td>
          <td class="js-sort-number"><strong>Date</strong></td>
          <td class="js-sort-number"><strong><u>ALL</u></strong></td>
          <td class="js-sort-number"><strong>FQA</strong></td>
          <td class="js-sort-number"><strong>GPS</strong></td>
          <td class="js-sort-number"><strong>MWP</strong></td>
          <td class="js-sort-number"><strong>TQA</strong></td>
          <td class="js-sort-number"><strong>VQA</strong></td>
          <td class="js-sort-number"><strong>ALG</strong></td>
          <td class="js-sort-number"><strong>ARI</strong></td>
          <td class="js-sort-number"><strong>GEO</strong></td>
          <td class="js-sort-number"><strong>LOG</strong></td>
          <td class="js-sort-number"><strong>NUM</strong></td>
          <td class="js-sort-number"><strong>SCI</strong></td>
          <td class="js-sort-number"><strong>STA</strong></td>
      </tr>`;

      for (var key in data) {
        var entry = data[key];

        table += '<tr>';
        table += `<td>${key}</td>`;
        table += `<td><b>${entry.Model}</b></td>`;
        table += `<td>${entry.Method}</td>`;
        table += `<td><a href="${entry.Source}" class="ext-link" style="font-size: 16px;">Link</a></td>`;
        table += `<td>${entry.Date}</td>`;

        table += `<td><b>${entry.ALL}</b></td>`;

        table += `<td>${entry.FQA}</td>`;
        table += `<td>${entry.GPS}</td>`;
        table += `<td>${entry.MWP}</td>`;
        table += `<td>${entry.TQA}</td>`;
        table += `<td>${entry.VQA}</td>`;

        table += `<td>${entry.ALG}</td>`;
        table += `<td>${entry.ARI}</td>`;
        table += `<td>${entry.GEO}</td>`;
        table += `<td>${entry.LOG}</td>`;
        table += `<td>${entry.NUM}</td>`;
        table += `<td>${entry.SCI}</td>`;
        table += `<td>${entry.STA}</td>`;
        table += '</tr>';
    }

  table += '</table>';
  document.getElementById('testmini_leaderboard').innerHTML = table; // Assuming you have a div with id 'container' where the table will be placed
}

// Call the function when the window loads
window.onload = generateTable;
