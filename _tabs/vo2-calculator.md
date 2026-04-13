---
layout: page
icon: fas fa-calculator
order: 8
title: VO2 Calculator
---

This interactive calculator converts absolute VO2 to relative VO2, estimates METs, and summarizes how GET and RCP divide an exercise test into moderate, heavy, and severe intensity domains.

Values update automatically as you type. Time inputs use **minutes**, and decimals are allowed.

<div class="vo2-tool">
  <div class="vo2-grid">
    <div class="vo2-card">
      <h3>Inputs</h3>
      <div class="vo2-field">
        <label for="abs-vo2">Absolute VO2 (L/min)</label>
        <input id="abs-vo2" type="number" step="0.01" min="0" value="3.20">
      </div>
      <div class="vo2-field">
        <label for="body-mass">Body mass (kg)</label>
        <input id="body-mass" type="number" step="0.1" min="1" value="75.0">
      </div>
      <div class="vo2-field">
        <label for="get-time">GET time (min)</label>
        <input id="get-time" type="number" step="0.01" min="0" value="8.04">
      </div>
      <div class="vo2-field">
        <label for="rcp-time">RCP time (min)</label>
        <input id="rcp-time" type="number" step="0.01" min="0" value="16.50">
      </div>
      <div class="vo2-field">
        <label for="test-duration">Total test duration (min)</label>
        <input id="test-duration" type="number" step="0.01" min="0.1" value="20.00">
      </div>
      <button id="vo2-reset" type="button">Reset example values</button>
      <p class="vo2-note">Educational tool for coursework and portfolio use.</p>
    </div>

    <div class="vo2-card">
      <h3>Outputs</h3>
      <div class="vo2-results" id="vo2-results">
        <div class="vo2-result-box">
          <span class="vo2-result-label">Relative VO2</span>
          <strong id="relative-vo2">--</strong>
        </div>
        <div class="vo2-result-box">
          <span class="vo2-result-label">Estimated METs</span>
          <strong id="mets">--</strong>
        </div>
        <div class="vo2-result-box">
          <span class="vo2-result-label">GET (% of test)</span>
          <strong id="get-percent">--</strong>
        </div>
        <div class="vo2-result-box">
          <span class="vo2-result-label">RCP (% of test)</span>
          <strong id="rcp-percent">--</strong>
        </div>
      </div>

      <div class="vo2-phase-wrap">
        <div class="vo2-phase-bar" aria-label="Exercise intensity domains">
          <div id="phase-moderate" class="phase moderate"></div>
          <div id="phase-heavy" class="phase heavy"></div>
          <div id="phase-severe" class="phase severe"></div>
        </div>
        <div class="vo2-phase-labels">
          <span>Moderate</span>
          <span>Heavy</span>
          <span>Severe</span>
        </div>
      </div>

      <table class="vo2-table">
        <tbody>
          <tr>
            <th>Moderate domain</th>
            <td id="moderate-domain">--</td>
          </tr>
          <tr>
            <th>Heavy domain</th>
            <td id="heavy-domain">--</td>
          </tr>
          <tr>
            <th>Severe domain</th>
            <td id="severe-domain">--</td>
          </tr>
          <tr>
            <th>Interpretation</th>
            <td id="interpretation">--</td>
          </tr>
        </tbody>
      </table>

      <div id="vo2-warning" class="vo2-warning" hidden></div>
    </div>
  </div>
</div>

<style>
  .vo2-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.25rem;
    margin-top: 1rem;
  }

  .vo2-card {
    border: 1px solid rgba(127, 127, 127, 0.25);
    border-radius: 12px;
    padding: 1rem;
    background: rgba(127, 127, 127, 0.06);
  }

  .vo2-card h3 {
    margin-top: 0;
  }

  .vo2-field {
    margin-bottom: 0.9rem;
  }

  .vo2-field label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.3rem;
  }

  .vo2-field input {
    width: 100%;
    padding: 0.55rem 0.7rem;
    border-radius: 8px;
    border: 1px solid rgba(127, 127, 127, 0.4);
    background: transparent;
    color: inherit;
  }

  #vo2-reset {
    margin-top: 0.25rem;
    padding: 0.6rem 0.9rem;
    border-radius: 8px;
    border: 1px solid rgba(127, 127, 127, 0.4);
    background: transparent;
    color: inherit;
    cursor: pointer;
  }

  .vo2-note {
    font-size: 0.9rem;
    opacity: 0.8;
    margin-top: 0.8rem;
  }

  .vo2-results {
    display: grid;
    grid-template-columns: repeat(2, minmax(120px, 1fr));
    gap: 0.75rem;
    margin-bottom: 1rem;
  }

  .vo2-result-box {
    border: 1px solid rgba(127, 127, 127, 0.25);
    border-radius: 10px;
    padding: 0.75rem;
    background: rgba(127, 127, 127, 0.08);
  }

  .vo2-result-label {
    display: block;
    font-size: 0.9rem;
    margin-bottom: 0.3rem;
    opacity: 0.85;
  }

  .vo2-phase-wrap {
    margin: 1rem 0;
  }

  .vo2-phase-bar {
    display: flex;
    width: 100%;
    height: 22px;
    overflow: hidden;
    border-radius: 999px;
    border: 1px solid rgba(127, 127, 127, 0.25);
  }

  .phase {
    height: 100%;
  }

  .moderate {
    background: rgba(46, 204, 113, 0.75);
  }

  .heavy {
    background: rgba(241, 196, 15, 0.75);
  }

  .severe {
    background: rgba(231, 76, 60, 0.75);
  }

  .vo2-phase-labels {
    display: flex;
    justify-content: space-between;
    gap: 0.75rem;
    font-size: 0.9rem;
    margin-top: 0.45rem;
  }

  .vo2-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.75rem;
    table-layout: fixed;
  }

  .vo2-table th,
  .vo2-table td {
    padding: 0.7rem;
    border-top: 1px solid rgba(127, 127, 127, 0.2);
    text-align: left;
    vertical-align: top;
    overflow-wrap: anywhere;
    word-break: break-word;
  }

  .vo2-table th {
    width: 36%;
  }

  .vo2-table td {
    white-space: normal;
  }

  #interpretation {
    white-space: normal;
    overflow-wrap: anywhere;
  }

  .vo2-warning {
    margin-top: 1rem;
    padding: 0.75rem;
    border-radius: 8px;
    border: 1px solid rgba(231, 76, 60, 0.45);
    background: rgba(231, 76, 60, 0.12);
  }
</style>

<script>
  (() => {
    const defaults = {
      absVo2: 3.20,
      bodyMass: 75.0,
      getTime: 8.04,
      rcpTime: 16.50,
      testDuration: 20.00
    };

    const el = {
      absVo2: document.getElementById('abs-vo2'),
      bodyMass: document.getElementById('body-mass'),
      getTime: document.getElementById('get-time'),
      rcpTime: document.getElementById('rcp-time'),
      testDuration: document.getElementById('test-duration'),
      reset: document.getElementById('vo2-reset'),
      relativeVo2: document.getElementById('relative-vo2'),
      mets: document.getElementById('mets'),
      getPercent: document.getElementById('get-percent'),
      rcpPercent: document.getElementById('rcp-percent'),
      moderateDomain: document.getElementById('moderate-domain'),
      heavyDomain: document.getElementById('heavy-domain'),
      severeDomain: document.getElementById('severe-domain'),
      interpretation: document.getElementById('interpretation'),
      moderateBar: document.getElementById('phase-moderate'),
      heavyBar: document.getElementById('phase-heavy'),
      severeBar: document.getElementById('phase-severe'),
      warning: document.getElementById('vo2-warning')
    };

    const readNumber = (node) => Number.parseFloat(node.value);
    const fmt = (value, digits = 2) => Number.isFinite(value) ? value.toFixed(digits) : '--';

    function showWarning(message) {
      el.warning.hidden = false;
      el.warning.textContent = message;
    }

    function clearWarning() {
      el.warning.hidden = true;
      el.warning.textContent = '';
    }

    function resetOutputs() {
      el.relativeVo2.textContent = '--';
      el.mets.textContent = '--';
      el.getPercent.textContent = '--';
      el.rcpPercent.textContent = '--';
      el.moderateDomain.textContent = '--';
      el.heavyDomain.textContent = '--';
      el.severeDomain.textContent = '--';
      el.interpretation.textContent = '--';
      el.moderateBar.style.width = '0%';
      el.heavyBar.style.width = '0%';
      el.severeBar.style.width = '0%';
    }

    function update() {
      clearWarning();
      resetOutputs();

      const absVo2 = readNumber(el.absVo2);
      const bodyMass = readNumber(el.bodyMass);
      const getTime = readNumber(el.getTime);
      const rcpTime = readNumber(el.rcpTime);
      const testDuration = readNumber(el.testDuration);

      if (![absVo2, bodyMass, getTime, rcpTime, testDuration].every(Number.isFinite)) {
        showWarning('Enter a valid number in every field to generate outputs.');
        return;
      }

      if (absVo2 <= 0 || bodyMass <= 0 || testDuration <= 0) {
        showWarning('Absolute VO2, body mass, and total test duration must all be greater than zero.');
        return;
      }

      if (getTime < 0 || rcpTime < 0) {
        showWarning('GET and RCP times cannot be negative.');
        return;
      }

      if (getTime > testDuration || rcpTime > testDuration) {
        showWarning('GET and RCP must fall within the total test duration.');
        return;
      }

      if (rcpTime < getTime) {
        showWarning('RCP should occur at the same time as, or after, GET.');
        return;
      }

      const relativeVo2 = (absVo2 * 1000) / bodyMass;
      const mets = relativeVo2 / 3.5;
      const getPercent = (getTime / testDuration) * 100;
      const rcpPercent = (rcpTime / testDuration) * 100;

      const moderateDuration = getTime;
      const heavyDuration = rcpTime - getTime;
      const severeDuration = testDuration - rcpTime;

      el.relativeVo2.textContent = `${fmt(relativeVo2)} mL/kg/min`;
      el.mets.textContent = `${fmt(mets)} METs`;
      el.getPercent.textContent = `${fmt(getPercent, 1)}%`;
      el.rcpPercent.textContent = `${fmt(rcpPercent, 1)}%`;

      el.moderateDomain.textContent = `0.00 to ${fmt(getTime)} min (${fmt(getPercent, 1)}% of test)`;
      el.heavyDomain.textContent = `${fmt(getTime)} to ${fmt(rcpTime)} min (${fmt(heavyDuration)} min span)`;
      el.severeDomain.textContent = `${fmt(rcpTime)} to ${fmt(testDuration)} min (${fmt(severeDuration)} min span)`;

      el.moderateBar.style.width = `${Math.max(getPercent, 0)}%`;
      el.heavyBar.style.width = `${Math.max(rcpPercent - getPercent, 0)}%`;
      el.severeBar.style.width = `${Math.max(100 - rcpPercent, 0)}%`;

      let interpretation = `A relative VO2 of ${fmt(relativeVo2)} mL/kg/min corresponds to approximately ${fmt(mets)} METs.`;
      interpretation += ` GET occurs at ${fmt(getPercent, 1)}% of the test and RCP occurs at ${fmt(rcpPercent, 1)}%.`;
      interpretation += ` This places the heavy domain between ${fmt(getTime)} and ${fmt(rcpTime)} minutes.`;
      el.interpretation.textContent = interpretation;
    }

    function resetForm() {
      el.absVo2.value = defaults.absVo2;
      el.bodyMass.value = defaults.bodyMass;
      el.getTime.value = defaults.getTime;
      el.rcpTime.value = defaults.rcpTime;
      el.testDuration.value = defaults.testDuration;
      update();
    }

    [el.absVo2, el.bodyMass, el.getTime, el.rcpTime, el.testDuration].forEach((node) => {
      node.addEventListener('input', update);
    });

    el.reset.addEventListener('click', resetForm);
    update();
  })();
</script>
