row = '''
<div class="row">
    <div class="form-group"><p style="text-align: center; color: black;"><strong>${question}</strong></p></div>
    <div class="col-xs-12 col-md-12"><img src="${urli}" width="100%"/></div>
    <div class="col-xs-12 col-md-12"><br></div>
    <div class="form-group">
        <label style="margin-left: 9em">
            <input autocomplete="off" id="option1" name="questioni" type="radio" value="option1" required="">
            Option (1)
        </label>
        <label style="margin-left: 14em">
            <input autocomplete="off" id="option2" name="questioni" type="radio" value="option2">
            Option (2)
        </label>
        <label style="margin-left: 14em">
            <input autocomplete="off" id="option3" name="questioni" type="radio" value="option3">
            Option (3)
        </label>
        <label style="margin-left: 14em">
            <input autocomplete="off" id="option4" name="questioni" type="radio" value="option4">
            Option (4)
        </label>
    </div>
</div>
'''

for i in range(1, 49):
    print(row.replace("urli", f"url{i}").replace("questioni", f"question{i}"))