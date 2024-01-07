row = '''
<div class="row">
    <p style="text-align: center; color: black;"><strong>Question i/50</strong></p>
    <div class="form-group"><p style="text-align: center; color: black;"><strong>${question}</strong></p></div>
    <div class="col-xs-12 col-md-12"><img src="${urli}" width="100%"/></div>
    <div class="col-xs-12 col-md-12"><br></div>
    <div class="form-group">
        <label style="margin-left: 9em">
            <input autocomplete="off" id="option1" name="questioni" type="radio" value="option1" required="">
            Option (1)
        </label>
        <label style="margin-left: 20em">
            <input autocomplete="off" id="option2" name="questioni" type="radio" value="option2">
            Option (2)
        </label>
        <label style="margin-left: 20em">
            <input autocomplete="off" id="option3" name="questioni" type="radio" value="option3">
            Option (3)
        </label>
    </div>
</div>

'''

for i in range(1, 51):
    print(row.replace("urli", f"url{i}").replace("questioni", f"question{i}").replace("Question i", f"Question {i}"))