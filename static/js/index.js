

        var colors = [
            { Name: "Black" },
            { Name: "Blue" },
            { Name: "Brown" },
            { Name: "Green" },
            { Name: "Orange" },
            { Name: "Purple" },
            { Name: "Red" },
            { Name: "White" },
            { Name: "Yellow" }
        ];

        $(function () {


            $("#checkboxSelectCombo").igCombo({
                width: "270px",
                dataSource: colors,
                textKey: "Name",
                valueKey: "Name",
                multiSelection: {
                    enabled: true,
                    showCheckboxes: true
                }
            });

        });

   
