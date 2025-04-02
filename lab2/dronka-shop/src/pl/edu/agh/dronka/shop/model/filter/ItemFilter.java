package pl.edu.agh.dronka.shop.model.filter;

import pl.edu.agh.dronka.shop.model.Item;

import java.util.Map;

public class ItemFilter {

	private Item itemSpec = new Item();

	public Item getItemSpec() {
		return itemSpec;
	}
	public boolean appliesTo(Item item) {
		if (itemSpec.getName() != null
				&& !itemSpec.getName().equals(item.getName())) {
			return false;
		}
		if (itemSpec.getCategory() != null
				&& !itemSpec.getCategory().equals(item.getCategory())) {
			return false;
		}

		// applies filter only if the flag (secondHand) is true)
		if (itemSpec.isSecondhand() && !item.isSecondhand()) {
			return false;
		}

		// applies filter only if the flag (polish) is true)
		if (itemSpec.isPolish() && !item.isPolish()) {
			return false;
		}

        Map<String, Object> details = itemSpec.getDetails();

		if (details != null){
			for (String s : details.keySet()) {
                if (details.get(s) instanceof Boolean){
                    if (!item.getDetails().get(s).equals(details.get(s))) {
                        return false;
                    }
                }
			}
		}

		return true;
	}

}